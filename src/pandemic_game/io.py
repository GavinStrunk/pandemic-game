import yaml


def load_cities(cities_file: str) -> dict:
    with open(cities_file, 'r') as file:
        data = yaml.safe_load(file)

    return data
