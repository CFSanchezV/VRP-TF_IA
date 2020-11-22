from time import process_time
from constants import show_constants, optimals
from initialSolution import downloadData, uselocalData
import simulatedAnnealing as SA


def print_nodes(nodes):
    print("Nodes:")
    for node in nodes:
        print(node)


def main():
    show_constants()
    # solucion inicial
    # capacity, nodes, optimal_idx = uselocalData("data/E-n101-k14.vrp")
    capacity, nodes, optimal_idx = downloadData()
    optimal_value = optimals[optimal_idx]
        
    print("Nodos:")
    for node in nodes:
        print(node)
    print("Capacidad: ", capacity)

    initial_solution = SA.greedy_sol(nodes, capacity)
    costo_inicial = SA.costo_solucion(initial_solution, nodes)
    print("Costo solucion inicial:")
    print(costo_inicial)
    
    print(optimal_value)
    

if __name__ == "__main__":
    main()
