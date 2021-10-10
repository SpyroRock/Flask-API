import requests

location = {"London": {"woeid": 44418}, 
            "San Francisco": {"woeid": 2487956},
            "San Diego": {"woeid": 2487889}}

data = [0, 0, 0]
for l in range(len(data)):
    loc = input("Insert a Location London, San Francisco, San Diego: --> ")
    woeid = location[loc]["woeid"]

    date = input("Date: year/month/day: --> ")

    requests_forecast = requests.get(url="https://www.metaweather.com/api/location/"+ str(woeid) +"/"+ str(date) +"/")
    json_forecast_data = requests_forecast.json() 
    flag = True
    weather_info = {}
    for x in json_forecast_data:
        if flag:
            weather_info.update(x)
            del weather_info['id']
            data[l] = weather_info
            flag=False
        else:
            pass