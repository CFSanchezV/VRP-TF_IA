from time import process_time
from constants import show_constants
from initialSolution import downloadData, uselocalData
import simulatedAnnealing as SA


def print_nodes(nodes):
    print("Nodes:")
    for node in nodes:
        print(node)


def main():
    show_constants()
    # solucion inicial
    # capacity, nodes = uselocalData("data/A-n32-k5.vrp")
    capacity, nodes = downloadData()

    print("Nodos:")
    for node in nodes:
        print(node)
    print("Capacidad: ", capacity)

    initial_solution = SA.greedy_sol(nodes, capacity)
    costo_inicial = SA.costo_solucion(initial_solution, nodes)
    print("Costo solucion inicial:")
    print(costo_inicial)


def find_optimal_from_data():
    pass


if __name__ == "__main__":
    main()
