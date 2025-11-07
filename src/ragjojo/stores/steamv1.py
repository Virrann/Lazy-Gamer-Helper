from pickle import TRUE
import requests
import os

class steam:

    __url = f"https://api.steampowered.com/IFamilyGroupsService/GetSharedLibraryApps/v1/"

    def __api_key() -> str:
        return str(os.getenv("STEAM_WEBAPI_TOKEN"))
        
    def __id() -> str:
        return os.getenv("STEAM_ID")
    
    
    def get_family_games() -> requests.json(): 

        params = {
            "access_token": steam.__api_key(), 
            "family_groupid": 0,
            "include_own": True,
            "include_excluded": True,
            "include_free": True,
            "steamid": steam.__id()
        }

        resp = requests.get(steam.__url, params=params)
        return resp.json()
        
    