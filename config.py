encounters_9_0 = [
    {"id": 2398, "name": "Hurlaile"},
    {"id": 2418, "name": "Altimore"},
    {"id": 2383, "name": "Destructeur Affamé"},
    {"id": 2402, "name": "Le Roi Soleil"},
    {"id": 2405, "name": "Xy'mox"},
    {"id": 2406, "name": "Dame Innerva"},
    {"id": 2412, "name": "Le Conseil de Sang"},
    {"id": 2399, "name": "Fangepoing"},
    {"id": 2417, "name": "Les Généraux"},
    {"id": 2407, "name": "Dénathrius"}
]
encounters_9_1 = [
    {"id": 2423, "name": "Le Naphtrémens"},
    {"id": 2433, "name": "L'œil du Geôlier"},
    {"id": 2429, "name": "Les Neuf"},
    {"id": 2432, "name": "Vestige de Ner'zhul"},
    {"id": 2434, "name": "Étripeur d'âme Dormazain"},
    {"id": 2430, "name": "Mal-ferrant Raznal"},
    {"id": 2436, "name": "Gardien des Fondateurs"},
    {"id": 2431, "name": "Scribe du Desting Roh-Kalo"},
    {"id": 2422, "name": "Kel'Thuzad"},
    {"id": 2435, "name": "Sylvanas Coursevent"}
]

encounters = [
    {"id": 2512, "name": "Gardien Vigilant"},
    {"id": 2540, "name": "Dausegne"},
    {"id": 2553, "name": "Xy'mox"},
    {"id": 2544, "name": "Panthéon des Prototypes"},
    {"id": 2542, "name": "Skolex"},
    {"id": 2529, "name": "Halondrus" },
    {"id": 2539, "name": "Lihuvim" },
    {"id": 2546, "name": "Anduin" },
    {"id": 2543, "name": "Seigneurs de l'Effroi"},
    {"id": 2549, "name": "Rygelon"},
    {"id": 2537, "name": "Le JoJo"},
]



#waist => gants, ceinture, epau, bottes
#jewels => anneau et cou
#chest => jambe, torse, tête
#wirsts => poignets / cape.
gear_budget = {"waist_b": {200: 90, 213: 98, 226: 106, 233: 109, 239: 114, 246: 117, 252: 120, 259: 124, 265: 127, 272: 131, 278: 134, 285: 138},
               "jewels_b": {200: 171, 213: 193, 226: 214, 233: 226, 239: 236, 246: 247, 252: 258, 259: 269, 265: 279, 272: 291, 278: 299, 285: 311},
               "chest_b": {200: 122, 213: 132, 226: 141, 233: 146, 239: 151, 246: 156, 252: 160, 259: 166, 265: 170, 272: 175, 278: 179, 285: 185},
               "wrists_b": {200: 67, 213: 73, 226: 79, 239: 85, 252: 91, 259: 93, 265: 95, 272: 98, 278: 101, 285: 104},
               "trinkets_b": {200: 89, 213: 95, 226: 101, 239: 108, 252: 115},
               "weapon_1h_b": {200: 60, 213: 65, 226: 69, 233: 72, 239: 75, 252: 80, 259: 83, 265: 85, 272: 87, 278: 90, 285: 92},
               "weapon_2h_b": {200: 122, 213: 132, 226: 140, 233: 145, 239: 151, 246: 156, 252: 161, 259: 165, 272: 175, 278: 179, 285: 185}
               }
inventory_to_b = {"SHOULDER": "waist_b",
                  "NECK": "jewels_b",
                  "HEAD": "chest_b",
                  "CHEST": "chest_b",
                  "WAIST": "waist_b",
                  "LEGS": "chest_b",
                  "FEET": "waist_b",
                  "HAND": "waist_b",
                  "WRIST": "wrists_b",
                  "FINGER": "jewels_b",
                  "TRINKET": "trinkets_b",
                  "CLOAK": "wrists_b",
                  "TWOHWEAPON": "weapon_2h_b",
                  "WEAPON": "weapon_1h_b",
                  "RANGEDRIGHT": "weapon_1h_b",
                  "SHIELD": "weapon_1h_b",
                  "HOLDABLE": "weapon_1h_b",
                  }
specs = [
    # chevalier de la mort
    {"specName": "Blood", "className": "DeathKnight", "spe": "Sang", "classe": "DK", "mask": [5], "metric": "dps"},
    {"specName": "Frost", "className": "DeathKnight", "spe": "Givre", "classe": "DK", "mask": [3, 5], "metric": "dps"},
    {"specName": "Unholy", "className": "DeathKnight", "spe": "Impie", "classe": "DK", "mask": [3, 5], "metric": "dps"},
    # dh
    {"specName": "Havoc", "className": "DemonHunter", "spe": "Dps", "classe": "DH", "mask": [4, 6], "metric": "dps"},
    {"specName": "Vengeance", "className": "DemonHunter", "spe": "Tank", "classe": "DH", "mask": [5], "metric": "dps"},
    # druid
    {"specName": "Balance", "className": "Druid", "spe": "Équi", "classe": "Druide", "mask": [2, 3, 4], "metric": "dps"},
    {"specName": "Feral", "className": "Druid", "spe": "Féral", "classe": "Druide", "mask": [2, 3, 4], "metric": "dps"},
    {"specName": "Guardian", "className": "Druid", "spe": "Gardien", "classe": "Druide", "mask": [2, 3, 4], "metric": "dps"},
    {"specName": "Restoration", "className": "Druid", "spe": "Restau", "classe": "Druide", "mask": [2, 3, 4], "metric": "hps"},
    # hunter
    {"specName": "BeastMastery", "className": "Hunter", "spe": "BM", "classe": "Chasseur", "mask": [3, 5], "metric": "dps"},
    {"specName": "Marksmanship", "className": "Hunter", "spe": "Précis", "classe": "Chasseur", "mask": [3, 5], "metric": "dps"},
    {"specName": "Survival", "className": "Hunter", "spe": "Survie", "classe": "Chasseur", "mask": [3, 5], "metric": "dps"},
    # mage
    {"specName": "Arcane", "className": "Mage", "spe": "Arcane", "classe": "Mage", "mask": [2, 5], "metric": "dps"},
    {"specName": "Fire", "className": "Mage", "spe": "Feu", "classe": "Mage", "mask": [2, 5], "metric": "dps"},
    {"specName": "Frost", "className": "Mage", "spe": "Givre", "classe": "Mage", "mask": [2, 5], "metric": "dps"},
    # monk
    {"specName": "Brewmaster", "className": "Monk", "spe": "Tank", "classe": "Moine", "mask": [2, 4, 5], "metric": "dps"},
    {"specName": "Mistweaver", "className": "Monk", "spe": "Tissebrume", "classe": "Moine", "mask": [2, 4, 5], "metric": "hps"},
    {"specName": "Windwalker", "className": "Monk", "spe": "Marchevent", "classe": "Moine", "mask": [2, 4, 5], "metric": "dps"},
    # pal
    {"specName": "Holy", "className": "Paladin", "spe": "Sacré", "classe": "Paladin", "mask": [3], "metric": "hps"},
    {"specName": "Protection", "className": "Paladin", "spe": "Protection", "classe": "Paladin", "mask": [3, 4, 6], "metric": "dps"},
    {"specName": "Retribution", "className": "Paladin", "spe": "Vindicte", "classe": "Paladin", "mask": [3, 4, 6], "metric": "dps"},
    # priest
    {"specName": "Discipline", "className": "Priest", "spe": "Discipline", "classe": "Prêtre", "mask": [2, 4], "metric": "hps"},
    {"specName": "Holy", "className": "Priest", "spe": "Sacré", "classe": "Prêtre", "mask": [2, 4], "metric": "hps"},
    {"specName": "Shadow", "className": "Priest", "spe": "Ombre", "classe": "Prêtre", "mask": [2, 4], "metric": "dps"},
    # rogue
    {"specName": "Assassination", "className": "Rogue", "spe": "Assassinat", "classe": "Voleur", "mask": [4, 5], "metric": "dps"},
    {"specName": "Outlaw", "className": "Rogue", "spe": "Pirate", "classe": "Voleur", "mask": [4, 5], "metric": "dps"},
    {"specName": "Subtlety", "className": "Rogue", "spe": "Finesse", "classe": "Voleur", "mask": [4, 5], "metric": "dps"},
    # shaman
    {"specName": "Elemental", "className": "Shaman", "spe": "Elem", "classe": "Chaman", "mask": [3, 5], "metric": "dps"},
    {"specName": "Enhancement", "className": "Shaman", "spe": "Amélio", "classe": "Chaman", "mask": [3, 5], "metric": "dps"},
    {"specName": "Restoration", "className": "Shaman", "spe": "Restau", "classe": "Chaman", "mask": [3, 5], "metric": "hps"},
    # warlock
    {"specName": "Affliction", "className": "Warlock", "spe": "Affli", "classe": "Démoniste", "mask": [3, 5], "metric": "dps"},
    {"specName": "Demonology", "className": "Warlock", "spe": "Demono", "classe": "Démoniste", "mask": [3, 5], "metric": "dps"},
    {"specName": "Destruction", "className": "Warlock", "spe": "Destru", "classe": "Démoniste", "mask": [3, 5], "metric": "dps"},
    # warrior
    {"specName": "Arms", "className": "Warrior", "spe": "Armes", "classe": "Guerrier", "mask": [2, 4], "metric": "dps"},
    {"specName": "Fury", "className": "Warrior", "spe": "Fureur", "classe": "Guerrier", "mask": [2, 4], "metric": "dps"},
    {"specName": "Protection", "className": "Warrior", "spe": "Protection", "classe": "Guerrier", "mask": [2, 4], "metric": "dps"},
]

offensive_sbps = [
    # Sb powers
    328266,
    329778,
    333950,
    333935,
    323074,
    323090,
    342156,
    323919,
    326514,
    326572,
    322721,
    320659,
    320660,
    319210,
    319191,
    325066,
    325069,
    331586,
    331584,
    336239,
    336243,
    319983,
    332753,
    319973,
    # 9.1
    352503,
    352786,
    352805,
    352110,
    351094,
    350899,
    350935,
    350936,
    352373,
    351750,
    352417,
    351146,
    351149,
    351488,
    351491,
    352186,
    352188

]

potency_conduits = {
    "DeathKnight": {
        "Blood": [338516, 337884],
        "Frost": [337822, 337934, 337988, 338501],
        "Unholy": [338553, 337980, 337381, 338566],
        "Covenants": [338664, 338628, 338651, 341344, ]},
    "Druid": {
        "Balance": [340708, 340706, 340720, 340719],
        "Feral": [340705, 340688, 340694, 340682],
        "Guardian": [340609, 340552],
        "Restoration": [340616, 340621, 340550, 340549],
        "Covenants": [341378, 341383, 341447, 341446]},
    "DemonHunter": {
        "Havoc": [339228, 339151, 339231, 339230],
        "Vengeance": [339423, 339231],
        "Covenants": [339895, 340028, 340063, 344358]},
    "Hunter": {
        "BeastMastery": [341440, 340876, 339704, 339750],
        "Marksmanship": [339924, 339973, 340033, 339920],
        "Survival": [341350, 341399, 341246, 341222],
        "Covenants": [339018, 339059, 339129, 339109]},
    "Mage": {
        "Arcane": [336873, 337240, 337192, 336886],
        "Fire": [341325, 337224, 336821, 336852],
        "Frost": [336569, 336522, 336472, 336460],
        "Covenants": [337058, 337087, 336999, 336992]},
    "Monk": {
        "Brewmaster": [337119, 337264],
        "Mistweaver": [336773, 337241, 336812, 337099],
        "Windwalker": [336526, 336598, 336452, 336616],
        "Covenants": [337286, 337301, 337295, 337303]},
    "Paladin": {
        "Holy": [339570, 339984, 339712, 339987, 338787], #this one has an endurance conduit that's too strong to pass
        "Protection": [340012, 340006],
        "Retribution": [339371, 339531, 339374, 339518],
        "Covenants": [340218, 340212, 340192, 340185]},
    "Priest": {
        "Discipline": [337790, 337786, 337778, 337891],
        "Holy": [337914, 338345, 337811, 337947],
        "Shadow": [338342, 338319, 338332, 338338],
        "Covenants": [337966, 338315, 337979, 338305]},
    "Rogue": {
        "Assassination": [341539, 341538, 341536, 341537],
        "Outlaw": [341542, 341546, 341543, 341540],
        "Subtlety": [341549, 341567, 341556, 341559],
        "Covenants": [341264, 341310, 341272, 341309]},
    "Shaman": {
        "Elemental": [338303, 338131, 345594, 338252],
        "Enhancement": [338325, 338322, 338331, 338318],
        "Restoration": [338329, 338343, 338346, 338339],
        "Covenants": [339182, 339185, 339186, 339183]},
    "Warlock": {
        "Affliction": [339576, 339455, 339500, 339481],
        "Demonology": [339578, 339656, 339845, 339766],
        "Destruction": [339892, 339896, 339890, 340041],
        "Covenants": [340229, 340316, 340268, 340348]},
    "Warrior": {
        "Arms": [335242, 335260, 339386, 335234],
        "Fury": [335234, 337162, 337214, 337302],
        "Protection": [337154, 339818, 335234],
        "Covenants": [339259, 339370, 339265, 339939]},
    "generic": [357902]
}

healing_sbps = [
    328266,
    329791,
    329781,
    329778,
    333950,
    333935,
    323074,
    323091,
    323095,
    323919,
    342156,
    326514,
    326572,
    322721,
    319210,
    319213,
    319191,
    325066,
    331586,
    331584,
    336239,
    336243,
    319983,
    332753,
    332754,
    319973,
    # 9.1
    352503,
    352786,
    352805,
    352110,
    351094,
    350899,
    350935,
    350936,
    352373,
    351750,
    352417,
    351146,
    351149,
    351488,
    351491,
    352186,
    352188,
    # 9.1 Heal only
    352502,
    352779,
    352806,
    352109,
    351093,
    352405,
    351747,
    352365,
    352187

]