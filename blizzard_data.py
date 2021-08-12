import tokenhandler
import requests
import os.path
import json

blizzard_token = tokenhandler.get_btoken()
wow_api_url = "https://eu.api.blizzard.com/data/wow/"


def retrieve_talents(blizzard_token,getmedia):
    blizzard_header = {'Authorization': blizzard_token, 'Battlenet-Namespace': "static-eu"}
    t_response = requests.get(wow_api_url + "talent/index?locale=fr_FR", headers=blizzard_header)
    if t_response.status_code == 404:
        return
    talents = t_response.json()['talents']
    talents_output = {}
    for talent in talents:
        response = requests.get(wow_api_url+"talent/"+str(talent['id']), headers=blizzard_header)
        if response.status_code == 404:
            print("talent not happy")
            return
        r = response.json()
        spell_id = int(r['spell']['id'])
        name = r['spell']['name']['fr_FR']
        talent_dir = "/talents/"
        path = os.path.curdir + talent_dir
        filename = path + str(spell_id) + '.jpg'
        if getmedia and not os.path.exists(filename):
            media_response = requests.get(wow_api_url+"media/spell/"+str(spell_id), headers=blizzard_header)
            if media_response.status_code == 404:
                print("media not happy ", wow_api_url+"media/spell/"+str(spell_id))
                return
            print(media_response.json())
            media_url = media_response.json()['assets'][0]['value']
            media = requests.get(media_url)

            if not os.path.isdir(path):
                os.mkdir(path)

            f = open(filename, "wb")
            f.write(media.content)
            f.close()
        if spell_id not in talents_output:
            talents_output[spell_id] = name
    output_file_name = "talents.json"
    of = open(output_file_name, "wt")
    of.write(json.dumps(talents_output))
    of.close()


def retrieve_soul_binds(blizzard_token):
    blizzard_header = {'Authorization': blizzard_token, 'Battlenet-Namespace': "static-eu"}
    response = requests.get(wow_api_url+"covenant/soulbind/index?locale=fr_FR", headers=blizzard_header)
    if response.status_code == 404:
        print("no soulbinds")
        return
    soulbinds = {}
    sbs = response.json()["soulbinds"]
    for sb in sbs:
        c_r = requests.get(wow_api_url+"covenant/soulbind/"+str(sb['id']), headers=blizzard_header)
        if c_r.status_code == 404:
            print('c chiant')
        c_id = c_r.json()['creature']['id']
        if sb['id'] not in soulbinds:
            soulbinds[sb['id']] = {"name": sb['name'], "c_id": c_id}

    file = open("soulbinds.json", 'wt')
    file.write(json.dumps(soulbinds))
    file.close()


def retrieve_conduits_powers(blizzard_token):
    blizzard_header = {'Authorization': blizzard_token, 'Battlenet-Namespace': "static-eu"}
    response = requests.get(wow_api_url+"covenant/conduit/index?locale=fr_FR", headers=blizzard_header)
    if response.status_code == 404:
        print("no conduits")
        return
    conduits = {}
    cs = response.json()["conduits"]
    for c in cs:
        # retrieve conduits spell ids, need it for wowhead tooltips
        c_r = requests.get(wow_api_url+"covenant/conduit/"+str(c['id']), headers=blizzard_header)
        spell_id = c_r.json()['ranks'][0]["spell_tooltip"]['spell']["id"]
        if spell_id not in conduits:
            conduits[spell_id] = {"name": c['name'], "c_id": c['id'], "type": "conduit"}
            cm_url = wow_api_url+"media/spell/"+str(spell_id)
            print(cm_url)
            conduit_media_request = requests.get(cm_url, headers=blizzard_header)
            if conduit_media_request.status_code == 404:
                print("no media for conduit")
            else:
                conduit_media_url = conduit_media_request.json()["assets"][0]["value"]
                cm = requests.get(conduit_media_url)
                path = os.path.curdir + "/conduits/"
                if not os.path.isdir(path):
                    os.mkdir(path)
                file = open(path + str(spell_id) + '.jpg', 'wb')
                file.write(cm.content)
                file.close()


    sbps_response = requests.get(wow_api_url + "tech-talent/index?locale=fr_FR", headers=blizzard_header)
    ss = sbps_response.json()["talents"]
    for sbp in ss:
        s_r = requests.get(wow_api_url + "tech-talent/"+str(sbp['id']), headers=blizzard_header)
        if "spell_tooltip" not in s_r.json():
            continue
        spell_id = s_r.json()["spell_tooltip"]["spell"]["id"]
        if spell_id not in conduits:
            conduits[spell_id] = {"name": sbp['name'], "c_id": sbp['id'], "type": "sbp" }
        s_media_r = requests.get(wow_api_url + "media/tech-talent/" + str(sbp['id']), headers=blizzard_header)
        media_url = s_media_r.json()["assets"][0]['value']
        media = requests.get(media_url)
        path = os.path.curdir+"/conduits/"
        if not os.path.isdir(path):
            os.mkdir(path)
        file = open(path+str(spell_id)+'.jpg', 'wb')
        file.write(media.content)
        file.close()
    file = open("conduits.json", 'wt')
    file.write(json.dumps(conduits))
    file.close()

def retrieve_boss_images(blizzard_token):
    blizzard_header = {'Authorization': blizzard_token, 'Battlenet-Namespace': "static-eu"}
    response = requests.get(wow_api_url + "covenant/conduit/index?locale=fr_FR", headers=blizzard_header)




retrieve_talents(blizzard_token, True)
#retrieve_soul_binds(blizzard_token)
#retrieve_conduits_powers(blizzard_token)
