import requests

url = "https://api.met.no/weatherapi/locationforecast/2.0/complete?altitude=10&lat=66.1985&lon=13.0350"
headers = {"Accept": "application/json", "User-Agent": "MyWeatherApp/1.0 (odinelias07@gmail.com)"}

response = requests.get(url, headers=headers)

def mellomrom(num):
    for i in range(num):
        print("")

if response.status_code == 200:
    data = response.json()
    
    temperatur = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]
    vind = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["wind_speed"]
    vindkast = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["wind_speed_of_gust"]
    nedbør = data["properties"]["timeseries"][0]["data"]["next_1_hours"]["details"]["precipitation_amount"]
    torden = data["properties"]["timeseries"][0]["data"]["next_1_hours"]["details"]["probability_of_thunder"]

    vindEmoji = ""
    temperaturEmoji = ""

    if vind >= 10:
        vindEmoji = "🌪️"
    else:
        vindEmoji = "🍃"

    if temperatur >= 10:
        temperaturEmoji = "☀️"
    elif temperatur <= 10:
        temperaturEmoji = "🥶"   
    elif temperatur <= 0:
        temperaturEmoji = "⛄"

    mellomrom(1)
    print("Her er værforholdene på Nesna akkurat nå: ")
    print(f"Temperatur: {temperatur} °C {temperaturEmoji}")
    print(f"Vind: {vind } m/s, og {vindkast} m/s i vindkastene {vindEmoji}")
    print(f"Nedbør: {nedbør} mm")
    print(f"Det er også en {torden}% sjanse for torden!⚡")
else:
    print(f"Feil: {response.status_code}")
    print("Desverre får vi ikke til å hente været akkurat nå, men prøv igjen senere!😭")
