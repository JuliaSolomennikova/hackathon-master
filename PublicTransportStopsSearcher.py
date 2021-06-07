import requests
import CityTools
import json
from typing import NamedTuple
from typing import List
import math


class PublicTransportStop(NamedTuple):
    coordinates: List[float]

    def get_distance_to_point(self, coords: List[float]) -> float:
        if self.coordinates == coords:
            return 0
        l0 = coords[0] * math.pi / 180
        l1 = self.coordinates[0] * math.pi / 180
        f0 = coords[1] * math.pi / 180
        f1 = self.coordinates[1] * math.pi / 180
        distance = math.acos(math.sin(f0) * math.sin(f1)
                             + math.cos(f0) * math.cos(f1)
                             * math.cos(l0 - l1))
        radius = 6371
        return distance * radius


def find_all_public_transport_stops(city_name) -> List[PublicTransportStop]:
    stops_list: List[PublicTransportStop] = []
    skip = 0
    count = 500
    while True:
        url = CityTools.url_former(city_name, 'Остановка общественного транспорта', skip, count)
        answer = requests.get(url)
        for stop in answer.json()['features']:
            coordinates = stop['geometry']['coordinates']
            stops_list.append(PublicTransportStop([coordinates[0], coordinates[1]]))
        if len(answer.json()['features']) < count - 1:
            break
        else:
            skip += count
    return stops_list


def write_all_stops_to_json_file(city_name, file_name):
    stops_list = find_all_public_transport_stops(city_name)

    with open(file_name, 'w') as stops_file:
        json.dump(stops_list, stops_file)


def read_stops_from_json_file(file_name) -> List[PublicTransportStop]:
    with open(file_name, 'r') as stops_file:
        obj_list = json.load(stops_file)

    stops_list: List[PublicTransportStop] = []
    for obj in obj_list:
        stops_list.append(PublicTransportStop([obj[0][0], obj[0][1]]))

    return stops_list


# write_all_stops_to_json_file('Екатеринбург', 'stops.json')
