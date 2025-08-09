import requests

data = {
    "MedInc": 10.3252,
    "HouseAge": 41,
    "AveRooms": 6.9841,
    "AveBedrms": 1.0238,
    "Population": 322,
    "AveOccup": 2.5556,
    "Latitude": 37.88,
    "Longitude": -122.23
}

response = requests.post("http://localhost:5000/predict", json=data)
print(response.json())