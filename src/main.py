from lghelper.stores import *
import json

from dotenv import load_dotenv
load_dotenv()

response = steamv1.get_family_games()

print(json.dumps(response, indent=4))
