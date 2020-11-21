from mainClasses import Route, Node
import requests
import random as rnd

def print_solution(header, solution):
    try:
        int(solution[0])
        print(f"{header}: {solution}")
    except TypeError:
        print(f"{header}")
        print(solution)


def percent(a, b):
    return 100 * (a - b) / a


def main():
    s = "rfghg      sds fsf 444"

    print(s)
    s2 = s.replace('\t', ' ')
    # print(s[1:12])

    print(s2)

    print()
    print()

    costs = {}
    truck_id = 0
    nodes = [Node(0, 10, 1, 2), Node(1, 20, 3, 4), Node(2, 30, 5, 6)]

    clients_to_visit = [node.id for node in nodes[1:]]
    for id in clients_to_visit:
        client = nodes[id]
        cost = nodes[truck_id].distance_to_node(client.x, client.y)
        costs[id] = cost
        truck_id += 1

    print(costs)
    costs = sorted(costs.items(), key=lambda item: (item[1], item[0]))
    print(costs)



# from urllib.request import urlopen
# dfile = urlopen(url)
# for line in dfile:
#     # decoded_line = line.decode("utf-8")
#     print(type(line))


def parsing(path):
    with open(path) as file:        
        strFile = file.read()
        start = strFile.find("NODE_COORD_SECTION") + len("NODE_COORD_SECTION")
        end = strFile.find("DEMAND_SECTION")
        nodes = strFile[start:end].replace('\t', ' ')
    
    return nodes

urlA = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/A/A-n32-k5.vrp"
ulrB = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/B/B-n31-k5.vrp"
ulrE = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/E/E-n101-k14.vrp"
urlX = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/X/X-n101-k25.vrp"
urls = [urlA, ulrB, ulrE, urlX]

resp = requests.get(rnd.choice(urls), stream=True)

for line in resp.iter_lines(decode_unicode=True):
    print(line)

# with open("data/A-n32-k5.vrp") as file:
#     for line in file:
#         print(line, end="")

# nodos = parsing("data/A-n32-k5.vrp")
# for line in nodos:
#     print(line, end="")