from dataclasses import dataclass
import networkx as nx
from typing import List


@dataclass
class City:
    name: str
    color: str
    infection_cases: dict


@dataclass
class World:
    graph: nx.Graph
    cities: list


def create_world(cities_data: dict):
    # Create city objects and graph
    city_objs = []
    graph = nx.Graph()
    for city in cities_data['cities']:
        city_objs.append(City(name=city[0], color=city[1], infection_cases={}))
        graph.add_node(city[0])

    # Add connections to graph
    for city_name, conn_list in cities_data['connections']:
        for conn in conn_list:
            graph.add_edge(city_name, conn)

    w = World(graph=graph, cities=city_objs)
    return w

def get_connected_cities(world: World, city: City) -> List[City]:
    neighbors = list(world.graph.neighbors(city.name))
    return neighbors

def infect_city(city: City, virus: str):
    pass

# if __name__ == '__main__':
#     config = '../../config/cities.yaml'
#     data = load_cities(config)
#
#     print(data)
#
#     import matplotlib.pyplot as plt
#
#     nx.draw(data.graph, with_labels=True)
#     plt.show()