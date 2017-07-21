import folium, pandas

map = folium.Map(location=[47.73, -121.88], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="my map")

data = pandas.read_csv("Volcanoes.csv")

lat = list(data["LAT"])
lon = list(data["LON"])
info = list("Name: " + data["NAME"] + " | Status: " + data["STATUS"] + " | Type: " + data["TYPE"])
time = list(data["TIMEFRAME"])

# fg.add_child(folium.Marker(location=[47.73, -121.88], popup="This is a marker", icon=folium.Icon(color="blue")))
# fg.add_child(folium.Marker(location=[46.73, -120.88], popup="This is a marker", icon=folium.Icon(color="blue")))
#
# for i in range(len(lat)):
#     fg.add_child(folium.Marker(location=(int(lat[i]),int(lon[i])), popup=name[i], icon=folium.Icon(color="blue")))

def color_select(tm):
    if tm == "D7":
        return "red"
    elif tm == "D6":
        return "orange"
    elif tm == "U":
        return "blue"
    elif tm == "D2":
        return "yellow"
    elif tm == "Q":
        return "purple"
    elif tm == "D3":
        return "grey"
    elif tm == "D4":
        return "black"
    elif tm == "D1":
        return "pink"
    else:
        return "green"

for lt,ln,nf,tm in zip(lat, lon, info, time):
    fg.add_child(folium.Marker(location=(lt,ln), popup=nf, icon=folium.Icon(color=color_select(tm))))

map.add_child(fg)

map.save("map1.html")
