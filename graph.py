import matplotlib.pyplot as plt
from constants import set_xy_labels
# from initialSolution import downloadData
# import simulatedAnnealing as SA


def live_subplot(nodes, solution, axis, axis_title):
    if not plt.isinteractive():
        plt.ion()
        plt.show()

    axis.clear()
    axis.set_title(axis_title, fontsize=16)
    set_xy_labels(axis)
    subplot_solution(nodes, solution, axis)
    plt.pause(0.5)  # pause in secs


def live_plot(nodes, solution):
    if not plt.isinteractive():
        plt.ion()
        plt.show()
    plt.clf()
    plot_solution(nodes, solution)
    plt.pause(0.5)  # pause in secs


def draw_line(x1, y1, x2, y2, color):
    x_values = [x1, x2]
    y_values = [y1, y2]

    # plot the number in the list and set the line thickness.
    plt.plot(x_values, y_values, linewidth=1.5, color=color)


def draw_subline(x1, y1, x2, y2, color, axis):
    x_values = [x1, x2]
    y_values = [y1, y2]

    # plot the number in the list and set the line thickness.
    axis.plot(x_values, y_values, linewidth=1.5, color=color)


# plot nodes & depot
def plot_scatter(nodes):
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

    plt.title("Mejor solucion", fontsize=20)

    # draw dots
    x_lst = []
    y_lst = []
    for cli in clients:
        x_lst.append(cli.x)
        y_lst.append(cli.y)

    plt.scatter(x_lst, y_lst, s=40, color='g', marker="s")

    plt.scatter(depot.x, depot.y, s=100, color='r', marker='*')

    # draw truck lines
    d_pos = depot
    truck_id = 0
    colors = ['b', 'r', 'c', 'm', 'y', 'b']
    for node_id in solution:
        color = colors[truck_id % len(colors)]
        node_pos = nodes[node_id]
        draw_line(d_pos.x, d_pos.y, node_pos.x, node_pos.y, color)
        # keep going
        d_pos = node_pos
        # change truck
        if node_id == 0:
            truck_id += 1


def subplot_solution(nodes, solution, axis):
    depot = nodes[0]
    clients = nodes[1:]

    # draw dots
    x_lst = []
    y_lst = []
    for cli in clients:
        x_lst.append(cli.x)
        y_lst.append(cli.y)

    axis.scatter(x_lst, y_lst, s=40, color='g', marker="s")

    axis.scatter(depot.x, depot.y, s=100, color='r', marker='*')

    # draw truck lines
    d_pos = depot
    truck_id = 0
    colors = ['b', 'r', 'c', 'm', 'y', 'b']
    for node_id in solution:
        color = colors[truck_id % len(colors)]
        node_pos = nodes[node_id]
        draw_subline(d_pos.x, d_pos.y, node_pos.x, node_pos.y, color, axis)
        # keep going
        d_pos = node_pos
        # change truck
        if node_id == 0:
            truck_id += 1


def draw_solution(nodes, solution):
    depot = nodes[0]
    clients = nodes[1:]

    plt.title("¡¡Solución final!!", fontsize=15)

    # draw dots
    x_lst = []
    y_lst = []
    for cli in clients:
        x_lst.append(cli.x)
        y_lst.append(cli.y)

    plt.scatter(x_lst, y_lst, s=40, color='g', marker="s")

    plt.scatter(depot.x, depot.y, s=100, color='r', marker='*')

    # draw truck lines
    truck_id = 0
    d_pos = depot
    # colors = ['b', 'g' 'r', 'c', 'm', 'y', 'k', 'b']
    colors = ['b', 'r', 'c', 'm', 'y', 'b']
    for node_id in solution:
        color = colors[truck_id % len(colors)]
        node_pos = nodes[node_id]
        draw_line(d_pos.x, d_pos.y, node_pos.x, node_pos.y, color)
        # keep going
        d_pos = node_pos
        # change truck
        if node_id == 0:
            truck_id += 1

    plt.show()


# tests drawing
# if __name__ == "__main__":
#     pass
    # unit
    # draw_line(1, 2, 3, 4, 'b')
    # plt.show()

    # integral
    # capacity, nodes, optimal_idx = downloadData()
    # optimal_value = optimals[optimal_idx]
    # initial_solution = SA.greedy_sol(nodes, capacity)
    # plot_solution(nodes, initial_solution)
    # plt.show()
