from time import process_time, sleep
from constants import show_constants
from initialSolution import downloadData, uselocalData, optimals
import graph as gf
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
    # Clientes y capacidad de camiones
    print_nodes(nodes)
    print("Capacidad: ", capacity)

    initial_solution = SA.greedy_sol(nodes, capacity)
    costo_inicial = SA.costo_solucion(initial_solution, nodes)
    print("Costo solucion inicial:")
    print(costo_inicial)
    
    print(optimal_value)
        
    gf.live_plot(nodes, initial_solution)
    
    # end isinteractive
    if gf.plt.isinteractive():
        gf.plt.ioff()
        
    

if __name__ == "__main__":
    main()
