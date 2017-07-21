import folium

map = folium.Map(location=[47.73, -121.88], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="my map")

# fg.add_child(folium.Marker(location=[47.73, -121.88], popup="This is a marker", icon=folium.Icon(color="blue")))
# fg.add_child(folium.Marker(location=[46.73, -120.88], popup="This is a marker", icon=folium.Icon(color="blue")))

for coords in [[47.73, -121.88],[46.73, -120.88],[45.73, -121.38]]:
    fg.add_child(folium.Marker(location=coords, popup="This is a marker", icon=folium.Icon(color="blue")))


map.add_child(fg)

map.save("map1.html")
