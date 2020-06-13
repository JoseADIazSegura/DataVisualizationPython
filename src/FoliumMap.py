import pandas as pd

m = pd.read_csv("../data/hospital_beds_USA_v1.csv")

import folium
map = folium.Map(location=[37.0902,-95.7129 ], zoom_start=4,tiles='cartodbpositron')

for lat, lon,state,type in zip(m['lat'], m['lng'],m['state'],m['type']):
    folium.CircleMarker([lat, lon],
                        radius=5,
                        color='red',
                      popup =(
                    'State: ' + str(state) + '<br>'),

                        fill_color='red',
                        fill_opacity=0.7 ).add_to(map)
map