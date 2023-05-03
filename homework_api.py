import requests
import json


"""Giphy """


# def search_giphy(query):
#     api_key = '<YOUR_API_KEY>'
#     url = f'https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={query}&limit=5'
#
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = json.loads(response.text)
#         gif_urls = [item['images']['downsized_large']['url'] for item in data['data']]
#         return gif_urls
#     else:
#         return None
#
#
# query = input('Enter a search query: ')
# gif_urls = search_giphy(query)
#
# if gif_urls:
#     print(f'Results for "{query}":')
#     for url in gif_urls:
#         print(url)
# else:
#     print('No results found.')


"""API-weather"""


# api_key = "98b668476be6a51b108efd96e728ba8f"
# url = "https://api.openweathermap.org/data/2.5/weather"
#
# location = input("Введіть місто: ")
# params = {
#     "q": location,
#     "appid": api_key,
#     "units": "metric",
#     "lang": "ua"
# }
#
# response = requests.get(url, params=params)
#
# if response.status_code == 200:
#     data = response.json()
#     print(f"Погода у місті {data['name']}:")
#     print(f"\tТемпература: {data['main']['temp']}°C")
#     print(f"\tВідчувається як: {data['main']['feels_like']}°C")
#     print(f"\tМінімальна температура: {data['main']['temp_min']}°C")
#     print(f"\tМаксимальна температура: {data['main']['temp_max']}°C")
#     print(f"\tВологість: {data['main']['humidity']}%")
#     print(f"\tТиск: {data['main']['pressure']} гПа")
#     print(f"\tОпис: {data['weather'][0]['description']}")
# else:
#     print("Помилка підключення до серверу погоди")



"""notify"""


response = requests.get("http://api.open-notify.org/astros.json")

if response.status_code == 200:
    data = response.json()
    print("Number of astronauts in space:", data["number"])
    print("Names of astronauts in space:")
    for astronaut in data["people"]:
        print(astronaut["name"])
else:
    print("Unable to retrieve astronaut data")