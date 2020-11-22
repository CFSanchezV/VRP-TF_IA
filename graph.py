import matplotlib.pyplot as plt
from initialSolution import formatter, downloadData
from datetime import datetime
import simulatedAnnealing as SA



def draw_line(x1, y1, x2, y2, color):
    x_values = [x1, x2]
    y_values = [y1, y2]

    # plot the number in the list and set the line thickness.
    plt.plot(x_values, y_values, linewidth=2, color=color)


def draw_scatter(nodes):
    depot = nodes[0]
    clients = nodes[1:]

    # draw dots
    plt.scatter(depot.x, depot.y, s=10)

    x_lst = []
    y_lst = []
    for cli in clients:
        x_lst.append(cli.x)
        y_lst.append(cli.y)
    plt.scatter(x_lst, y_lst, s=10)

    plt.title("Destinos", fontsize=20)


def plot_solution(nodes, solution):
    depot = nodes[0]
    clients = nodes[1:]

    # draw dots
    plt.scatter(depot.x, depot.y, s=50, color='r')

    x_lst = []
    y_lst = []
    for cli in clients:
        x_lst.append(cli.x)
        y_lst.append(cli.y)
    plt.scatter(x_list, y_list, s=50, color='g')

    plt.title("Mejor solucion", fontsize=20)

    # draw truck lines
    # d_pos = depot
    truck_id = 0
    colors = ['b', 'r', 'c', 'm', 'y', 'b']
    for node_id in solution:
        color = colors[truck_id % len(colors)]
        node_pos = nodes[node_id]
        draw_line(depot.x, depot.y, node_pos.x, node_pos.y, color)
        # keep going
        depot = node_pos
        # change truck
        if node_id == 0:
            truck_id += 1

    plt.show()


# tests drawing
if __name__ == "__main__":
    # unit
    draw_line(1, 2, 3, 4, 'b')
    plt.show()
    
    # integral
    capacity, nodes, optimal_idx = downloadData()
    # optimal_value = optimals[optimal_idx]
    initial_solution = SA.greedy_sol(nodes, capacity)
    solution = formatter(initial_solution)
    plot_solution(nodes, solution)
    plt.show()
