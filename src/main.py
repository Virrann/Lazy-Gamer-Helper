from ragjojo.stores import steamv1
import json

from dotenv import load_dotenv
load_dotenv()

response = steamv1.steam.get_data()

print(json.dumps(response, indent=4))
