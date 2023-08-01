import json
from jinja2 import Environment, FileSystemLoader
from urllib.parse import quote
from urllib.request import urlopen


# prepare
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('scaffold.txt')
output_file="allesda.md"
output_string=""


#load data.json file
with open('types.json') as json_file:
    types = json.load(json_file)
    for type in types:
        query=template.render({'query': type["query"]})
        encoded_query=quote(query)
        data_url="https://overpass-api.de/api/interpreter?data="+encoded_query
        print("==== "+type["einzahl"]+" ====")
        print("json: "+data_url)
        print("query: "+query)  
        print()
        map_url="https://overpass-turbo.eu/map.html?Q="+encoded_query
        #load json from url
        with urlopen(data_url) as url:
            result=json.loads(url.read())
            count=len(result["elements"])
            if(count>0):
                if count==1:
                    output_string+="[1 "+type["einzahl"]+"]("+map_url+"), "
                else:
                    output_string+="["+str(count)+" "+type["mehrzahl"]+"]("+map_url+"), "
with open(output_file, "w") as text_file:
    text_file.write(output_string)
