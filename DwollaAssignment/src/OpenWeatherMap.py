import requests, json

# API Key
api = "bc620ead2d18122876f00d05d2993999"

# Base url
base = "http://api.openweathermap.org/data/2.5/weather?"

# Prompt city (only grab first word inputed)
city = raw_input("Where are you: ").split(' ', 1)[0]

# Api request url
url = base + "appid=" + api + "&q=" + city

# Units in Farenheight
params = {'units': 'imperial'}

# Get city data
response = requests.get(url, params=params)

# Convert json format into python format
data = response.json()

# If city was retrieved
if data["cod"] != "404":
    print(data["main"])
    temp = str(data["main"]["temp"])
    print(city+" weather:\n" + temp + " degrees Farenheit")

else:
    print("Could not retrieve city")