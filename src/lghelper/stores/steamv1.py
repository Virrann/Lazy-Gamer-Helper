import requests
import os
from pathlib import Path
from typing import Dict, Any

__url = f"https://api.steampowered.com/IFamilyGroupsService/GetSharedLibraryApps/v1/"
__id_file = "./data/steamids.lock"

def __api_key() -> str:
    return str(os.getenv("STEAM_WEBAPI_TOKEN"))
    
def __id() -> str:
    return os.getenv("STEAM_ID")

def update_id_list(apps) -> (list[int], list[int]):
    path = Path(__id_file)

    appids = [str(game["appid"]) for game in apps if "appid" in game]


    if not path.exists():

        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(appids))
        
        appids = [int(a) for a in appids]

        return appids, []
        
    else:

        with open(path, "r", encoding="utf-8") as f:
            existing_appids = [line.strip() for line in f.readlines()]

        current_set = set(appids)
        existing_set = set(existing_appids)

        added = [int(a) for a in (current_set - existing_set)]
        removed = [int(r) for r in (existing_set - current_set)]

        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(appids))

        return added, removed
        

def get_games_change()-> (Dict[str, Any], Dict[str, Any]): 

    params = {
        "access_token": __api_key(), 
        "family_groupid": 0,
        "include_own": True,
        "include_excluded": True,
        "include_free": True,
        #"max_apps": 1, # parameter only for debug
        "steamid": __id()
        
    }

    resp = requests.get(__url, params=params)

    resp = resp.json()

    apps = resp["response"]["apps"]

    added, removed = update_id_list(apps)

    apps_added = [a for a in apps if a["appid"]in added]

    apps_removed = [a for a in apps if a["appid"]in removed]
    

    return apps_added, apps_removed
        
    