#!/usr/bin/env python3
import json
from jinja2 import Environment, FileSystemLoader
from urllib.parse import quote
from urllib.request import urlopen

import requests
import requests_cache


# prepare
import sys
if len(sys.argv) > 1:
    area=sys.argv[1]
else:
    area="Winterthur"
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('scaffold.txt')
output_file="allesda.md"
output_string=f"# In {area} gibt es... \n\n"
requests_cache.install_cache('cache')


#process
with open('types.json') as json_file:
    types = json.load(json_file)
    for type in types:
        query=template.render({'query': type["query"],'area': area})
        encoded_query=quote(query)
        data_url="https://overpass-api.de/api/interpreter?data="+encoded_query
        print("\n\n\n\n==== "+type["einzahl"]+" ====")
        print("json: "+data_url)
        print("query: "+query)  
        map_url="https://overpass-turbo.eu/map.html?Q="+encoded_query
        with requests.get(data_url) as response:
            result = response.json()
            count=len(result["elements"])
            print("count: "+str(count))
            if(count>0):
                if type["approximate"]==True:
                    prefix="~"
                else:
                    prefix=""
                if count==1:
                    output_string+="["+prefix+"1 "+type["einzahl"]+"]("+map_url+"), "
                else:
                    output_string+="["+prefix+str(count)+" "+type["mehrzahl"]+"]("+map_url+"), "


# output
output_string=output_string[:-2]
output_string+="\n\nDaten von [OpenStreetmap](https://www.openstreetmap.org/), Quellcode auf [GitHub](https://github.com/blemli/allesda)."
with open(output_file, "w") as text_file:
    text_file.write(output_string)
