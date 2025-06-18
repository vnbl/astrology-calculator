import requests

url = "https://astrologer.p.rapidapi.com/api/v4/birth-data"

payload = { "subject": {
		"year": 1980,
		"month": 12,
		"day": 12,
		"hour": 12,
		"minute": 12,
		"longitude": 0,
		"latitude": 51.4825766,
		"city": "London",
		"nation": "GB",
		"timezone": "Europe/London",
		"name": "John Doe",
		"zodiac_type": "Tropic",
		"sidereal_mode": None,
		"perspective_type": "Apparent Geocentric",
		"houses_system_identifier": "P"
	} }
headers = {
	"x-rapidapi-key": "xxxxxxxxxxxxxx",
	"x-rapidapi-host": "astrologer.p.rapidapi.com",
	"Content-Type": "application/json",
	"X-RapidAPI-Host": "astrologer.p.rapidapi.com",
	"Accept": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())