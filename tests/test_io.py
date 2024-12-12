import pandemic_game.io as io


def test_load_cities():
    cities_file = '../config/cities.yaml'
    cities = io.load_cities(cities_file=cities_file)
    assert 'cities' in cities.keys()
    assert 'connections' in cities.keys()
    assert len(cities['cities']) == 48
    assert len(cities['connections']) == 48
