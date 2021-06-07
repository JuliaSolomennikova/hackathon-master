from typing import NamedTuple, List
import requests
import math
import CityTools


class BankBranch(NamedTuple):
    coordinates: List[float]
    address: str

    # closest_bus_station: int
    # metro_station_near: int
    # closest_shopping_mall: int
    # closest_office: int
    # is_bus_station_near: bool
    # is_metro_station_near: bool
    # is_shopping_mall_near: bool
    # is_office_near: bool

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


def find_all_bank_branches(city_name) -> List[BankBranch]:
    bank_branches: List[BankBranch] = []
    count = 500
    skip = 0
    while True:
        url = CityTools.url_former(city_name, 'Сбербанк России, отделения', skip, count)
        answer = requests.get(url)
        for feature in answer.json()['features']:
            bank_branch_coordinates = feature['geometry']['coordinates']
            bank_branch_address = feature['properties']['CompanyMetaData']['address']
            bank_branches.append(BankBranch([bank_branch_coordinates[0], bank_branch_coordinates[1]],
                                            address=bank_branch_address))
        if len(answer.json()['features']) < count - 1:
            break
        else:
            skip += count
    return bank_branches
