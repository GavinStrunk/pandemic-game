import networkx as nx
import pandemic_game.world as world


# Test data
config_file = '../config/cities.yaml'  # Update this path to your test config file

def test_load_cities():
    w = world.load_cities(config_file)
    assert isinstance(w, world.World)
    assert len(w.cities) > 0

def test_city_properties():
    w = world.load_cities(config_file)
    for city in w.cities:
        assert isinstance(city, world.City)
        assert isinstance(city.name, str)
        assert city.name  # Name should not be empty
        assert isinstance(city.color, str)
        assert isinstance(city.infection_cases, dict)

def test_city_connections():
    w = world.load_cities(config_file)
    graph = w.graph
    for city in w.cities:
        assert city.name in graph.nodes

        # Optionally, test for specific connections if known
        # for connected_city in known_connections[city.name]:
        #     assert graph.has_edge(city.name, connected_city)

def test_world_properties():
    w = world.load_cities(config_file)
    assert isinstance(w.graph, nx.Graph)
    assert len(w.graph.nodes) > 0

def test_getting_neighbors():
