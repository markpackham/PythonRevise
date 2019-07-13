#need to do "pip install pandas" to get the pandas python library
#pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools

import folium
import pandas as pd 
import os

states = os.path.join('data','us-states.json')
unemployment_data = os.path.join('data','us_unemployment.csv')
state_data = pd.read_csv(unemployment_data)

m = folium.Map(location=[48,-102],zoom_start=3)

m.choropleth(
    geo_data = states,
    name='choropleth',
    data=state_data,
    columns = ['State','Unemployment'],
    key_on='feature.id',
    fill_color='YlGn', #greenish yellow colors
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate %'
)

folium.LayerControl().add_to(m)

#creates our html file
m.save('employment.html')