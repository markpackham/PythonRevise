import folium
#os is like the path module for node.js
import os
import json

#To see the stuff at work you must install folium via pip
#To generate the html file run "python map.py"

#Create map object
m = folium.Map(location=[42.3601,-71.0589], zoom_start=12)

#Vega data (vega visualization)
vis = os.path.join('data','vis.json')

#Geojason Data, get json file from our data folder
overlay = os.path.join('data','overlay.json')

#Global tooltip variable
tooltip = 'Click for more info'

#Create custom marker icon
logoIcon = folium.features.CustomIcon('logo.png',icon_size=(50,50))

#Create markers, "m" is the map
folium.Marker([42.363600,-71.099500],
popup='<strong>Location One</strong>',
tooltip=tooltip).add_to(m),
folium.Marker([42.333600,-71.099500],
popup='<strong>Location Two</strong>',
tooltip=tooltip,
icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([42.377120,-71.099500],
popup='<strong>Location Three</strong>',
tooltip=tooltip,
icon=folium.Icon(color='purple')).add_to(m)
folium.Marker([42.374150,-71.199500],
popup='<strong>Location Four</strong>',
tooltip=tooltip,
icon=folium.Icon(color='green', icon='leaf')).add_to(m),
folium.Marker([42.375140,-71.179500],
popup='<strong>Location Five</strong>',
tooltip=tooltip,
icon=logoIcon).add_to(m),
folium.Marker([42.315140,-71.072450],
icon=folium.Icon(color='orange'),
popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)),width=450,height=250))).add_to(m)

#Circle marker
folium.CircleMarker(
    location=[42.384150,-70.982110],
    radius=50,
    popup='A circle',
    color='red',
    fill=True,
    fill_color='yellow'
).add_to(m)

#Geojson overlay
folium.GeoJson(overlay,name='cambridge').add_to(m)

#Generate map
m.save('map.html')