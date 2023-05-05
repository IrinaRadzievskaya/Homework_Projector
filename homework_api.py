import requests
import json


def get_response(u, p={}):
	response = requests.get(u, p)
	response.raise_for_status()
	return response.json()


"""Giphy """


def search_giphy(search_term):
	api_key = '<YOUR_API_KEY>'
	url = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_term}&limit=5"
	data = get_response(url)
	gifs = data["data"]
	for gif in gifs:
		url = gif["images"]["downsized_large"]["url"]
		print(url)


search_term = input('Enter a search query: ')
search_giphy(search_term)


"""API-weather"""


# def get_weather(city):
# 	api_key = "98b668476be6a51b108efd96e728ba8f"
#
# 	url = "https://api.openweathermap.org/data/2.5/weather"
# 	params = {
#         "q": city,
#         "appid": api_key,
#         "units": "metric",
#         "lang": "ua"
#     }
# 	data = get_response(url, params)
# 	print(f"Погода у місті {data['name']}:")
# 	print(f"\tТемпература: {data['main']['temp']}°C")
# 	print(f"\tВідчувається як: {data['main']['feels_like']}°C")
# 	print(f"\tМінімальна температура: {data['main']['temp_min']}°C")
# 	print(f"\tМаксимальна температура: {data['main']['temp_max']}°C")
# 	print(f"\tВологість: {data['main']['humidity']}%")
# 	print(f"\tТиск: {data['main']['pressure']} гПа")
# 	print(f"\tОпис: {data['weather'][0]['description']}")
#
#
# location = input("Введіть місто: ")
# get_weather(location)



"""notify"""


# def notify():
# 	url = "http://api.open-notify.org/astros.json"
# 	data = get_response(url)
# 	print("Number of astronauts in space:", data["number"])
# 	print("Names of astronauts in space:")
# 	for astronaut in data["people"]:
# 		print(astronaut["name"])
#
#
# notify()
