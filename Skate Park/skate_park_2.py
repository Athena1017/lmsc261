import json

data_json = open("ramps.json")
data_dict = json.load(data_json)

for k in data_dict:
    v = data_dict[k]
    print(f"{k}s favorite ramp is {v}")
    