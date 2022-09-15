import json
import pandas as pd
import pygal.maps.world
from pygal.maps.world import COUNTRIES

url = 'https://github.com/owid/covid-19-data/blob/master/public/data/latest/owid-covid-latest.json'

covid19 = pd.read_html(url)

file = json.loads(covid19[0][1].values.tolist()[0])
data = pd.DataFrame(file).transpose()[['location','new_cases', 'last_updated_date']].reset_index()
codebook = pd.Series(COUNTRIES, name = 'location').reset_index()
data_coded = data.merge(codebook, how = 'left', on='location', suffixes =('_data','_map'))

value = dict(zip(data_coded.index_map, data_coded.new_cases))

# Create map
title = "Daily Cases for covid 19 over the world, updated on "+ str(max(data_coded.last_updated_date)[:10])
worldmap = pygal.maps.world.World()
worldmap.title = title
worldmap.add( "New cases", value)
worldmap.render_to_file('covid19.svg')

'''
data = {}
date = []

for code, info in file.items():
    data.update(dict(zip([info["location"]], [info["new_cases"]])))
    date.append(info['last_updated_date'])

value = {}

for country, new_cases in data.items():
    for refcode, refname in COUNTRIES.items():
        if refname == country:
            countrycode = refcode
            if countrycode != None:
                value[countrycode] = new_cases


'''