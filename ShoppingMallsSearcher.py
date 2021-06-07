import requests
import CityTools
from typing import NamedTuple
from typing import List


class ShoppingMall(NamedTuple):
    coordinates: List[float]


api_key = 'c070b7eb-119b-40b1-80bc-00e16124bd35'


def find_all_shopping_malls(city_name, has_more_than_n_companies) -> List[ShoppingMall]:
    raise Exception('Not implemented yet')
    malls_list: List[ShoppingMall] = []
    skip = 0
    count = 500
    while True:
        url = CityTools.url_former(city_name, 'Торговый центр', skip, count)
        answer = requests.get(url)
        for mall in answer.json()['features']:
            coordinates = mall['geometry']['coordinates']
            malls_list.append(ShoppingMall([coordinates[0], coordinates[1]]))
        if len(answer.json()['features']) < count - 1:
            break
        else:
            skip += count
    return malls_list
    return 0

answer = requests.get('https://search-maps.yandex.ru/v1/?apikey=' + api_key
                      + '&type=biz&lang=ru_RU&ll=60.600269,56.828609&spn=0.001,0.001&results=500')
print(len(answer.json()['features']))
for feature in answer.json()['features']:
    print(feature['properties']['CompanyMetaData']['name'])