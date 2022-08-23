import json
import pygal.maps.world
from pygal.maps.world import COUNTRIES

path = 'covid19_daily.json'

with open(path) as file:
    covid = json.load(file)
data = {}
for code, info in covid.items():
    data.update(dict(zip([info["location"]], [info["new_cases"]])))

'''def getcountrycode(country):
    for refcode, refname in COUNTRIES.items():
        if refname == country:
            return refcode
    return None
'''
value = {}
'''for country, new_cases in data.items():
    countrycode = getcountrycode(country)
    if countrycode != None:
        value[countrycode] = new_cases'''

for country, new_cases in data.items():
    for refcode, refname in COUNTRIES.items():
        if refname == country:
            countrycode = refcode
            if countrycode != None:
                value[countrycode] = new_cases

worldmap = pygal.maps.world.World()
worldmap.title = "Daily Cases for covid 19 over the world"
worldmap.add("New cases", value)
worldmap.render_to_file('covid19.svg')
