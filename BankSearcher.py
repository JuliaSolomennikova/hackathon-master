import requests
import pprint

api_key = 'c070b7eb-119b-40b1-80bc-00e16124bd35'
answer = requests.get('https://search-maps.yandex.ru/v1/?apikey='+api_key
                      +'&lang=ru_RU&text=Екатеринбург, Сбербанк России, отделения&results=500')

print('Found '+str(len(answer.json()['features'])))
for feature in answer.json()['features']:
    print(feature['properties']['CompanyMetaData']['name']+': '+feature['properties']['CompanyMetaData']['address'])
