from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import json
import os.path
import tokenhandler
import config
import requests
import logging
import datetime

logging.basicConfig(filename="wcl-data.log", level=logging.WARNING, format='%(asctime)s:%(message)s')
token = tokenhandler.get_token()
blizzard_token = tokenhandler.get_btoken()
blizzard_header = {'Authorization': blizzard_token, 'Battlenet-Namespace': "static-eu"}
headers = {'Authorization': token}
secondary_stats = ["CRIT_RATING", "HASTE_RATING", "MASTERY_RATING", "VERSATILITY"]
# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://www.warcraftlogs.com/api/v2/client", headers=headers)
# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)
query_string = """
    query ($encounterId: Int!,$metric: CharacterRankingMetricType!,$className: String!,$specName: String!)
    {
      worldData
      {
        encounter(id:$encounterId)
        {
            characterRankings(metric:$metric,className:$className,specName:$specName,includeCombatantInfo:true)
        }
      }
    }
    """


def scaleItemLvl(item, real_ilvl):
    if real_ilvl == item['api_ilvl']:
        return item['stats']
    start_budget_value = 0
    if item['type'] not in config.inventory_to_b:
        return
    else:
        gear_type = config.inventory_to_b[item['type']]
    for stat in item['stats']:
        start_budget_value += item['stats'][stat]
    budget = config.gear_budget[gear_type]
    # if we find the ilvl of the gear in the template budgets
    if real_ilvl in budget:
        budget_value = budget[real_ilvl]
    else:
        # else we compute the actual budget based on what it should be approximately.
        upper = 1000
        lower = -1
        for b_ilvl in budget:
            if real_ilvl < b_ilvl < upper:
                upper = b_ilvl
            if real_ilvl > b_ilvl > lower:
                lower = b_ilvl
        if lower == -1:
            c_b_diff = list(budget)[1] - list(budget)[0]
            keys = list(budget.keys())
            ilvl_diff = keys[1] - keys[0]
            budget_value = budget[keys[0]] + (c_b_diff/ilvl_diff)*(real_ilvl-keys[0])
        # now that lower and upperbound have been found
        elif upper == 1000:
            max_i = len(budget)-1
            c_b_diff = list(budget)[max_i] - list(budget)[max_i-1]
            keys = list(budget.keys())
            ilvl_diff = keys[max_i] - keys[max_i-1]
            budget_value = budget[keys[max_i]] + (c_b_diff / ilvl_diff) * (real_ilvl - keys[max_i])
        else:
            share = (real_ilvl - lower) / (upper - lower)
            budget_value = budget[lower] + round((budget[upper] - budget[lower]) * share)
    factor = budget_value / start_budget_value
    scaled_stats = {}
    for stat in item['stats']:
        scaled_stats[stat] = round(item['stats'][stat]*factor)
    return scaled_stats


def get_blizzard_data(item_id):
    response = requests.get("https://eu.api.blizzard.com/data/wow/item/"+str(item_id), headers=blizzard_header)
    item_stats = {}
    if response.status_code == 404:
        return "none"
    api_ilvl = response.json()['level']
    inventory_type = response.json()['inventory_type']['type']
    if 'stats' not in response.json()['preview_item']:
        return "none" # handle legendary in a better way.
    for stat in response.json()['preview_item']['stats']:
        if stat["type"]["type"] in secondary_stats:
            item_stats[stat["type"]["type"]] = stat["value"]
    item = {"id": item_id, "type": inventory_type, "api_ilvl": api_ilvl, "stats": item_stats}
    return item


# Make it into a standard string that represents stat priorities. the goal is to represent things such H>V>M>C
# or H=V>M=C or yet again H>V=M>C.
def computeStatsPriorities(player_sstat_budget):
    priorities = ""
    # find out an order, and relationships.
    total = 0
    for stat in player_sstat_budget:
        total += player_sstat_budget[stat]
    stats_sorted = sorted(player_sstat_budget.items(), key=lambda item: item[1], reverse=True)
    i = 0
    if total == 0:
        return
    for stat in stats_sorted:
        if i > 0:
            if (stats_sorted[i-1][1]/total)-(stats_sorted[i][1]/total) < 0.03:
                priorities += ">="
            else:
                priorities += ">"
        priorities += stat[0][:1]
        i += 1
    return priorities


# the goal of this is to get blizz data from the item list we already have, or from the blizz api,
# then scale it and return it
def get_item_data(item_id, ilvl):
    if item_id == 0:
        return
    if item_id not in items:
        # store an ITEM
        item = get_blizzard_data(item_id)
        items[item_id] = item
    else:
        item = items[item_id]
    if item == "none":
        return
    if not items[item_id]['stats']:
        return
    # scale an item
    return scaleItemLvl(items[item_id], ilvl)


# storing this to create a master list of what is played on all bosses.
def store_result(result, className, specName):
    if className in results:
        if specName in results[className]:
            results[className][specName].extend(result)
        else:
            results[className][specName] = result
    else:
        results[className] = {specName: result}




def get_data(gql_client, query_parameters):
    query = gql(query_string)
    result = gql_client.execute(query, variable_values=query_parameters)
    # store_result(result['worldData']['encounter']['characterRankings']['rankings'], query_parameters['className'],
    # ll
    # query_parameters['specName'])
    return combine_data(result['worldData']['encounter']['characterRankings']['rankings'], query_parameters)


def combine_conduits_sbps(powers, conduits, spec):
    # take soulbind powers and conduits, filter them according to usefulness, and make a combination
    combination = []
    if spec['metric'] == "dps":
        filtered_sbps = config.offensive_sbps
    else:
        filtered_sbps = config.healing_sbps
    potency_conduits = config.potency_conduits[spec["className"]][spec["specName"]] + \
                       config.potency_conduits[spec["className"]]["Covenants"] + \
                       config.potency_conduits["generic"]


    # filter to keep only the interesting powers
    for power in powers:
        if power['id'] in filtered_sbps:
            combination.append(power['id'])
    for conduit in conduits:
        if conduit['id'] in potency_conduits:
            combination.append(conduit['id'])
    # this orders conduits by id
    c_combo_id = ""
    combination.sort()
    for item in combination:
        c_combo_id += str(item)
    c_combo_id = hash(c_combo_id)
    return c_combo_id, combination


def combine_data(data, query_parameters):
    # Kiryan, Venthyr, Fae, Necro.
    talent_combinations = {'covenant_list': [0, 0, 0, 0], 'combos': {}}
    p = 1
    for player in data:
        talent_array = player['talents']
        talent_combinations['covenant_list'][player['covenantID']-1] = talent_combinations['covenant_list'][player['covenantID']-1] + 1
        talent_combination = {'talents': talent_array, 'id': ""}
        # this computes the talent combination : this believes talents are provided in the right order
        # which, should it fail is easy to fix : always order them before concatenation.
        i = 0
        for talent in talent_array:
            i = i + 1
            if i in query_parameters['mask']:
                continue
            talent_combination['id'] += str(talent['id'])
        # this orders legendaries by id, and computes an id
        legendaries = sorted(player["legendaryEffects"], key=lambda x: x['id'])
        lgds_id = ""
        for lgd in legendaries:
            legs.add(lgd["id"])
            lgds_id += str(lgd["id"])
        # talent combination includes legendaries.
        talent_combination['id'] += lgds_id
        tc_id = hash(talent_combination['id'])
        lgds_id = hash(lgds_id)
        # this part computes the stat budget.
        player_sstat_budget = {"CRIT_RATING": 0, "HASTE_RATING": 0, "MASTERY_RATING": 0, "VERSATILITY": 0}
        gems = {173127: {"stat": "CRIT_RATING", "value": 16},
                173128: {"stat": "HASTE_RATING", "value": 16},
                173130: {"stat": "MASTERY_RATING", "value": 16},
                173129: {"stat": "VERSATILITY", "value": 16}}
        for item in player['gear']:
            if 'id' not in item or "itemLevel" not in item:
                continue
            item_stats = get_item_data(item['id'], int(item['itemLevel']))
            if not item_stats:
                continue

            for stat_type in item_stats:
                # player_sstat_budget[stat_type] += item_stats[stat_type] (original version, the one below weights for higher ranks)
                player_sstat_budget[stat_type] += round(item_stats[stat_type] * (1 - ((p - 1) / 100)))
            if 'gems' in item:
                for gem in item['gems']:
                    if int(gem['id']) in gems:
                        player_sstat_budget[gems[int(gem['id'])]["stat"]] += round((gems[int(gem['id'])]["value"]) *
                                                                                   (1 - ((p - 1) / 100)))
        # soulbind powers and conduit combo computation. Since there is a bit of code, pushing it out to a function
        c_combo_id, combination = combine_conduits_sbps(player["soulbindPowers"], player["conduitPowers"], query_parameters)
        combos = talent_combinations['combos']
        clist = [0, 0, 0, 0]
        clist[player['covenantID']-1] += 1
        if tc_id not in combos:
            combos[tc_id] = {'tc': talent_combination,
                             'count': 1,
                             'rank': p,
                             'covenant_list': clist,
                             'stat_priorities': {'total_budget': player_sstat_budget,'prio': computeStatsPriorities(player_sstat_budget)},
                             'conduits': {c_combo_id: {'count': 1, 'rank': p, 'combination': combination, 'sbid': player['soulbindID']}},
                             'legendaries': player["legendaryEffects"]}
        else:
            #dealing with the covenant
            combos[tc_id]['covenant_list'][player['covenantID']-1] += 1
            # increasing the count
            combos[tc_id]['count'] = combos[tc_id]['count'] + 1
            # dealing with soulbinds and conduits combinations
            if c_combo_id not in combos[tc_id]['conduits']:
                combos[tc_id]['conduits'][c_combo_id] = {'count': 1, 'rank':p,'combination': combination, 'sbid':player['soulbindID']}
            else:
                combos[tc_id]['conduits'][c_combo_id]['count'] += 1
            # dealing with stats priorities
            for stat in player_sstat_budget:
                combos[tc_id]['stat_priorities']['total_budget'][stat] += player_sstat_budget[stat]
            combos[tc_id]['stat_priorities']['prio'] = computeStatsPriorities(combos[tc_id]['stat_priorities']['total_budget'])

        p = p + 1


    return talent_combinations
# odn = "output"
# outdir = "./"+odn+"/"


odn = "data"
app_path = "/var/www/stratwow/wp-content/wcl-data/"
data_path = app_path+odn+"/"
if not os.path.isdir(data_path):
    os.makedirs(data_path)
spec_file = open(app_path+"index.json", "wt")
index = {'specs': config.specs, "encounters": config.encounters, "when": datetime.datetime.now().timestamp()}
spec_file.write(json.dumps(index))
spec_file.close()
items_file = 'items.json'
leg_file = 'leg.json'
if os.path.isfile(items_file):
    items = json.loads(open(items_file, 'rt').read())
else:
    items = {}
legs = set()
results = {}
for encounter in config.encounters:
    for spec in config.specs:
        spec['encounterId'] = encounter['id']
        # calling wcl to get data on encounters x specs
        output = get_data(client, spec)
        # saving data in several output files.
        filename = data_path+str(encounter['id'])+"-"+spec["className"]+"-"+spec["specName"]+".json"
        f = open(filename, "wt")
        f.write(json.dumps(output))
        f.close()
    logging.info("encounter : %s done", encounter['name'])

# writing the items file
open(items_file, 'wt').write(json.dumps(items))
open(leg_file, 'wt').write(json.dumps(list(legs)))