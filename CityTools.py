import requests
from typing import List

api_key = '99f02ee8-e627-48cd-9c08-e68c89d28783'
api_key = 'c070b7eb-119b-40b1-80bc-00e16124bd35'


def get_city_bounds(city_name) -> List[List[float]]:
    url = 'https://search-maps.yandex.ru/v1/?apikey=' + api_key + \
          '&lang=ru_RU&text=' + city_name + '&results=1'
    answer = requests.get(url)
    return answer.json()['features'][0]['properties']['boundedBy']


def url_former(city_name: str, what_to_search: str, skip: int, count: int) -> str:
    city_bounds = get_city_bounds(city_name)
    url = 'https://search-maps.yandex.ru/v1/?apikey=' + api_key + \
          '&lang=ru_RU&text=' + what_to_search + '&results=' + str(count) + \
          '&bbox=' + str(city_bounds[0][0]) + ',' + str(city_bounds[0][1]) + '~' + \
          str(city_bounds[1][0]) + ',' + str(city_bounds[1][1]) + \
          '&skip=' + str(skip)
    return url
