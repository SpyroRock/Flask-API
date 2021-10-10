import requests
from request_weather import data

BASE = "http://127.0.0.1:5000/"

# video_info = {"likes": 10, "name": "Tim", "views": 1000}

# data = [weather_info]
# print(weather_info)

# print(f"DATA1:{data[0]}\n")
# print(f"DATA2:{data[1]}\n")
# print(f"DATA3:{data[2]}\n")
# print(f"Length of data: {len(data)}")

for i in range(len(data)):
    response = requests.put(BASE + "weather/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "weather/2")
print(response.json())

input()
response = requests.post(BASE + "weather/1")
print(response.json())

# # # response = requests.patch(BASE + "video/2", {"views": 99, "likes":2999})

