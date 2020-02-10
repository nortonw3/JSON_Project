import csv

in_file = open('Australia_Fires_November_2019.csv', 'r')

csv_file = csv.reader(in_file, delimiter=",")

header = next(csv_file)

longs_i = 0
lats_i = 0
bright_i = 0

for index, column_header in enumerate(header):
    if column_header == "latitude":
        lats_i = index
    elif column_header == "longitude":
        longs_i = index
    elif column_header == "brightness":
        bright_i = index
    print(index, column_header)

print("Latitude Index: " + str(lats_i))
print("Longitude Index: " + str(longs_i))
print("Brightness Index: " + str(bright_i))

latitudes = []
longitudes = []
brightness = []

for row in csv_file:
    latitudes.append(float(row[lats_i]))
    longitudes.append(float(row[longs_i]))
    brightness.append(float(row[bright_i]))

print(max(brightness))
print(min(brightness))

import plotly.graph_objects as go
from plotly import offline

#fig = go.Figure(go.Scattergeo(lon=longitudes, lat=latitudes))
#fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig = go.Figure(data=go.Scattergeo(
        lon = longitudes,
        lat = latitudes,
        locationmode = 'country names',
        marker = dict(
            size=12,
            line = dict(
                width=1,
                color='rgba(255,255,255)'
            ),
            colorscale = 'YlGnBu',
            cmin = min(brightness),
            color = brightness,
            cmax = max(brightness),
            colorbar_title="Brightness"
        )))

fig.update_layout(
        title = 'Australian Fires - November 2019',
        geo = dict(
            scope='world',
        ),
    )


offline.plot(fig,filename='Australian_Fires_November_2019.html')