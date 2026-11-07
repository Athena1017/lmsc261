import json

def check_age_experience(skaters):
    for skater in skaters:
        name = skater.get('name', 'key not found')
        age = skater.get('age', 0)
        is_experienced = skater.get('is_experienced', False)

        if (age >= 13 and is_experienced):
            print(f"Hi {name}, welcome to the skate park!")

try:
    data_json = open("skaters.json")
    data_dict = json.load(data_json)
    check_age_experience(data_dict)

except FileNotFoundError:
    print("skaters.json was not found")
    