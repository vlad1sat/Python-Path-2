import requests
import json
from requests import Response


def get_pilots(pilots_information):
    pilots: list = list()

    for info_pilot in pilots_information:
        pilot_req: Response = requests.get(info_pilot)
        pilot: dict = json.loads(pilot_req.text)
        result_pilot: dict = {key: value for key, value in pilot.items() if key in ['name', 'height', 'mass']}

        homeworld_url: str = pilot['homeworld']
        homeworld_req: Response = requests.get(homeworld_url)
        homeworld: dict = json.loads(homeworld_req.text)
        result_pilot['homeworld'] = homeworld['name']
        result_pilot['homeworld_url'] = homeworld_url
        pilots.append(result_pilot)

    return pilots


if __name__ == '__main__':
    my_req: Response = requests.get('https://swapi.dev/api/starships/')
    ships: dict = json.loads(my_req.text)
    result: dict = dict()
    count_ship: int = 1

    for ship in ships['results']:
        result_ship: dict = dict()
        result_ship['ship-name'] = ship['name']
        result_ship['starship_class'] = ship['starship_class']
        result_ship['max_atmosphering_speed'] = ship['max_atmosphering_speed']
        result[f'ship-{count_ship}'] = result_ship
        count_ship += 1
        if len(ship['pilots']):
            result_ship['pilots'] = get_pilots(pilots_information=ship['pilots'])
        else:
            result_ship['pilots'] = ship['pilots']

    with open('result.json', 'w', encoding='utf-8') as result_file:
        json.dump(result, result_file, indent=4)
