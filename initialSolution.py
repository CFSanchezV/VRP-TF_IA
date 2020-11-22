from mainClasses import *
from copy import deepcopy
from constants import urls, optimals_dict, optimals
import requests
import random as rnd
import os


def separator(longStr, start, end):
    i = longStr.find(start) + len(start)
    j = longStr.find(end)
    # print(longStr[i:j])
    return longStr[i:j].replace('\t', ' ')


def uselocalData(localpath):
    with open(localpath, 'r') as file:
        strFile = file.read()

    name = os.path.basename(file.name)
    fLetter = name[0].lower()
    val = optimals_dict[fLetter]
    idx = optimals.index(val)

    node_strings = separator(
        strFile, "NODE_COORD_SECTION", "DEMAND_SECTION").split('\n')[1:-1]
    demand_strings = separator(
        strFile, "DEMAND_SECTION", "DEPOT_SECTION").split('\n')[1:-1]
    capacity_string = separator(strFile, "CAPACITY :", "NODE_COORD_SECTION")
    capacity = int(capacity_string.strip())
    # print(demand_strings)

    n_clients = len(demand_strings)
    nodes = []
    for i in range(n_clients):
        x, y = node_strings[i].strip().split(" ")[1:]
        demand = demand_strings[i].strip().split(" ")[-1]

        nodes.append(Node(i, demand, x, y))

    return capacity, nodes, idx


def downloadData():
    anyURL = rnd.choice(urls)
    resp = requests.get(anyURL, stream=True)
    strFile = resp.text
    idx = urls.index(anyURL)

    node_strings = separator(
        strFile, "NODE_COORD_SECTION", "DEMAND_SECTION").split('\n')[1:-1]
    demand_strings = separator(
        strFile, "DEMAND_SECTION", "DEPOT_SECTION").split('\n')[1:-1]
    capacity_string = separator(strFile, "CAPACITY :", "NODE_COORD_SECTION")
    capacity = int(capacity_string.strip())

    n_clients = len(demand_strings)
    nodes = []
    for i in range(n_clients):
        x, y = node_strings[i].strip().split(" ")[1:]
        demand = demand_strings[i].strip().split(" ")[-1]

        nodes.append(Node(i, demand, x, y))

    return capacity, nodes, idx


def greedy_sol(nodes, capacity):
    depot = nodes[0]  # depot: Node 0

    # setup clients and list of routes
    clients_to_visit = [node.id for node in nodes[1:]]
    routes = []

    while len(clients_to_visit) > 0:
        # truck w/ capacity = capacity
        truck_capacity = capacity
        truck_id = 0
        # first route, cost: 0
        route = Route([0])

        while True:
            # dict(k: id, v: cost)
            costs = {}
            for client_id in clients_to_visit:
                client = nodes[client_id]
                cost = nodes[truck_id].distance_to_node(
                    client.x, client.y)
                costs[client_id] = cost
            # sorted tuple list from smallest to biggest cost, [(client_id, cost),()]
            costs = sorted(costs.items(), key=lambda item: (item[1], item[0]))

            # next node = client or depot
            while len(costs) > 0:
                # pick first element
                candidate_id, candidate_cost = costs[0]
                costs = costs[1:]
                if nodes[candidate_id].demand <= truck_capacity:
                    # next node
                    next_node = nodes[candidate_id]
                    cost_to_next_node = candidate_cost
                    break
            else:
                # return to depot
                next_node = depot
                cost_to_next_node = nodes[truck_id].distance_to_node(
                    depot.x, depot.y)

            # go to next node and update truck, routes
            route.path.append(next_node.id)
            route.cost += cost_to_next_node
            truck_capacity -= next_node.demand
            truck_id = next_node.id

            if next_node.id in clients_to_visit:
                clients_to_visit.remove(next_node.id)

            # back to depot
            if truck_id == depot.id:
                break

        # store route in list
        routes.append(route)

    # return routes
    # format output
    return formatter(routes)


'''
Format 1
input list of Routes, start formatter  Ruta | Costo: 158, Camino: [0, 21, 16, 18, 25, 5, 4, 29, 8, 11, 0],
  Ruta | Costo: 115, Camino: [0, 28, 26, 12, 23, 7, 6, 0],
  Ruta | Costo: 240, Camino: [0, 22, 9, 13, 17, 30, 3, 2, 0],
  Ruta | Costo: 244, Camino: [0, 24, 19, 1, 15, 14, 10, 20, 0],
  Ruta | Costo: 188, Camino: [0, 27, 0]
]

output, list of Routes without 0s:
[
  Ruta | Costo: 158, Camino: [21, 16, 18, 25, 5, 4, 29, 8, 11],
  Ruta | Costo: 115, Camino: [28, 26, 12, 23, 7, 6],
  Ruta | Costo: 240, Camino: [22, 9, 13, 17, 30, 3, 2],
  Ruta | Costo: 244, Camino: [24, 19, 1, 15, 14, 10, 20],
  Ruta | Costo: 188, Camino: [27]
]

'''


def formatter(solution):
    solution_as_list = [0]
    for route in solution:
        solution_as_list += route.path[1:]
    return solution_as_list


'''
Format 2
input list of Routes, start and end with 0s:
[
  Ruta | Costo: 158, Camino: [0, 21, 16, 18, 25, 5, 4, 29, 8, 11, 0],
  Ruta | Costo: 115, Camino: [0, 28, 26, 12, 23, 7, 6, 0],
  Ruta | Costo: 240, Camino: [0, 22, 9, 13, 17, 30, 3, 2, 0],
  Ruta | Costo: 244, Camino: [0, 24, 19, 1, 15, 14, 10, 20, 0],
  Ruta | Costo: 188, Camino: [0, 27, 0]
]

output, list of integers:
[
  0, 21, 16, 18, 25, 5, 4, 29, 8, 11,
  0, 28, 26, 12, 23, 7, 6,
  0, 22, 9, 13, 17, 30, 3, 2,
  0, 24, 19, 1, 15, 14, 10, 20,
  0, 27, 0
]
'''
