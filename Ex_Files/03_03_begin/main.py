import csv
import json
from pprint import pprint

# python dictionary, isn't JSON yet
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN) # create json string
back_to_dict = json.loads(einstein_json) # convert back to dict
print(einstein_json)
pprint(back_to_dict)

# turns csv into a dict
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

# turns this into a json
with open("laureates.json", "w") as f:
    json.dump(laureates, f, indent=2)
