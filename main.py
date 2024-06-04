# GHATV6SZ9WFMVEBVMLNH5VBJ - recovery code
import requests
from twilio.rest import Client

URL = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "Api key"
account_sid = "Account id"
auth_token = "Authorization token"

parameter = {
    "lat": 18.520430,
    "lon": 73.856743,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(URL, params=parameter)
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's rainy outside, carry an umbrella ☂️",
        from_="+12183220577",
        to="Your Verified Number"
    )
    print(message.status)
