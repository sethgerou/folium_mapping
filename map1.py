import folium, pandas, random

map = folium.Map(location=[47.73, -121.88], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="my map")

data = pandas.read_csv("Volcanoes.csv")

lat = list(data["LAT"])
lon = list(data["LON"])
info = list("Name: " + data["NAME"] + " | Status: " + data["STATUS"] + " | Type: " + data["TYPE"])
time = list(data["TIMEFRAME"])
elev = list(data["ELEV"])

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
def radius_select(el):
    if el < 1000:
        return 5
    elif el < 2000:
        return 10
    elif el < 3000:
        return 15
    elif el < 4000:
        return 20
    else:
        return 25

for lt,ln,nf,tm,el in zip(lat, lon, info, time, elev):
    fg.add_child(folium.CircleMarker(location=(lt,ln), radius=radius_select(el), weight=2, popup=nf, color="black", fill_opacity=.7, fill_color=color_select(tm)))

map.add_child(fg)

map.save("map1.html")
