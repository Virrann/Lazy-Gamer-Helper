from lghelper.stores import *
import json
import os

from dotenv import load_dotenv
load_dotenv()

if os.path.exists(steamv1.__id_file):
    os.remove(steamv1.__id_file)

response = steamv1.get_games_change()

print(json.dumps(response, indent=4))

