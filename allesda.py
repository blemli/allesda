import json

#load data.json file
with open('data.json') as json_file:
    places = json.load(json_file)
    print(places)
    for name,query in places:
        print(name)