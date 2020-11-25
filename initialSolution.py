from mainClasses import Node, Route
from copy import deepcopy
from constants import urls, optimals_dict, optimals
import requests
import random as rnd
import os
from collections import OrderedDict

def get_solution_routes(solution_input):
    all_routes = []    
    route = []
    for i, sol in enumerate(solution_input[1:]):        
        l = len(route)

        if sol == 0 and l > 0 and solution_input[i-1] != 0:
            r = list(OrderedDict.fromkeys(route))
            all_routes.append(r)
            route = []
        elif sol !=0:
            route.append(sol)
        else:
            continue

    # list of lists of routes
    return all_routes

def separator(longStr, start, end):
    i = longStr.find(start) + len(start)
    j = longStr.find(end)
    # print(longStr[i:j])
    return longStr[i:j].replace('\t', ' ')


def uselocalData(localpath):
    try:
        with open(localpath, 'r') as file:
            strFile = file.read()

    except FileNotFoundError:
        print(f"\nLa ruta '{localpath}' no es una ruta válida")
        exit()

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

            # while len(clients_to_visit)
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


def formatter(solution):
    solution_lst = [0]
    for route in solution:
        # print(route)
        solution_lst += route.path[1:]
    # print("formatted solution: ", solution_lst)
    return solution_lst


'''
Format
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

# TESTING
# sol = [0, 26, 28, 23, 23, 7, 0, 0, 15, 11, 11, 14, 24, 1, 19, 29, 0, 2, 27, 10, 2, 10, 10, 20, 10, 0, 30, 22, 3, 6, 3, 6, 9, 0, 0, 0, 0, 21, 17, 13, 9, 8, 12, 0, 0, 4, 5, 16, 18, 25, 25, 25, 21, 0, 0, 0, 0, 0]
# print(sol)
# print("")
# get_solution_routes(sol)