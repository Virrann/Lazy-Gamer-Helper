import requests
import os
from pathlib import Path

__url = f"https://api.steampowered.com/IFamilyGroupsService/GetSharedLibraryApps/v1/"
__id_file = "./data/steamids.txt"

def __api_key() -> str:
    return str(os.getenv("STEAM_WEBAPI_TOKEN"))
    
def __id() -> str:
    return os.getenv("STEAM_ID")

def update_id_list(appids):
    path = Path(__id_file)


    if not path.exists():

        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(appids))

        return appids, []
        
    else:

        with open(path, "r", encoding="utf-8") as f:
            existing_appids = [line.strip() for line in f.readlines()]

        current_set = set(appids)
        existing_set = set(existing_appids)

        added = list(current_set - existing_set)
        removed = list(existing_set - current_set)

        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(appids))

        return added, removed
        

def get_family_games(): 

    params = {
        "access_token": __api_key(), 
        "family_groupid": 0,
        "include_own": True,
        "include_excluded": True,
        "include_free": True,
        #"max_apps": 1,
        "steamid": __id()
        
    }

    resp = requests.get(__url, params=params)
    resp = resp.json()

    apps = resp["response"]["apps"]

    appids = [str(game["appid"]) for game in apps if "appid" in game]

    

    return apps
        
    