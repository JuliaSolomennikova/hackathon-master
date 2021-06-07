import BankBranch
import PublicTransportStopsSearcher
from typing import NamedTuple
from typing import List
import pprint


class BankEntry(NamedTuple):
    coordinates: List[float]
    address: str
    nearest_bank_coordinates: List[float]
    nearest_bank_address: str
    distance_to_nearest_bank: float
    nearest_transport_stop_coordintaes: List[float]
    distance_to_nearest_transport_stop: float


def form_table(city_name) -> List[BankEntry]:
    table: List[BankEntry] = []
    bank_branches = BankBranch.find_all_bank_branches(city_name)
    stops_list = PublicTransportStopsSearcher.find_all_public_transport_stops(city_name)
    print('Banks count: ' + str(len(bank_branches)) + ' Stops count: ' + str(len(stops_list)))
    for bank in bank_branches:
        min_distance_to_bank = float('inf')
        for another_bank in bank_branches:
            distance = bank.get_distance_to_point(another_bank.coordinates)
            if distance != 0 and distance < min_distance_to_bank:
                nearest_bank_branch = another_bank
                min_distance_to_bank = distance

        min_distance_to_stop = float('inf')
        for stop in stops_list:
            distance = bank.get_distance_to_point(stop.coordinates)
            if distance < min_distance_to_stop:
                nearest_stop = stop
                min_distance_to_stop = distance

        table.append(
            BankEntry(bank.coordinates, bank.address, nearest_bank_branch.coordinates, nearest_bank_branch.address,
                      min_distance_to_bank, nearest_stop.coordinates, min_distance_to_stop))

    return table


result = form_table('Екатеринбург')
pprint.pprint(result)
