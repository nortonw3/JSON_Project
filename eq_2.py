import json

in_file = open('eq_data_1_day_m1.json', 'r')
out_file = open('readable_eq_data.json', 'w')

eq_data = json.load(in_file)

print(type(eq_data))

json.dump(eq_data, out_file, indent=4)

list_of_eqs = eq_data['features']

print(type(list_of_eqs))

print(len(list_of_eqs))

mags = []
longs = []
lats = []

for eq in list_of_eqs:
    mags.append(eq['properties']['mag'])
    longs.append(eq['geometry']['coordinates'][0])
    lats.append(eq['geometry']['coordinates'][1])

print(mags[:10])

from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

#data = [Scattergeo(lon=longs,lat=lats)]

data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'marker': {
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title="GLobal Earthquakes")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='global_earthquakes.html')