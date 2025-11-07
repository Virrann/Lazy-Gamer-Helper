import requests
import os

__url = f"https://api.steampowered.com/IFamilyGroupsService/GetSharedLibraryApps/v1/"

def __api_key() -> str:
    return str(os.getenv("STEAM_WEBAPI_TOKEN"))
    
def __id() -> str:
    return os.getenv("STEAM_ID")


def get_family_games(): 

    params = {
        "access_token": __api_key(), 
        "family_groupid": 0,
        "include_own": True,
        "include_excluded": True,
        "include_free": True,
        "steamid": __id()
    }

    resp = requests.get(__url, params=params)
    return resp.json()
        
    