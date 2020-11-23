from time import process_time
from constants import show_constants, rutas_locales, percent_diff, print_nodes
from initialSolution import downloadData, uselocalData, optimals
import graph
import simulatedAnnealing as SA


def validar_input(veces_a_aplicar, ruta_archivo):
    try:
        veces = int(veces_a_aplicar)
        ruta = str(ruta_archivo)
    except ValueError:
        print("Ruta o número de iteraciones inválido")
        exit()
    if ruta == "":
        print("Ruta vacía, descargando datos aleatorios de CVRPLIB")
    return veces, ruta


def main():
    print("\n---------------INICIALIZACIÓN---------------\n")
    veces_a_aplicar = input("Ingresar # de iteraciones: ")
    print("Lista de archivos:", rutas_locales)
    ruta_archivo = input(
        "Ingresar ruta de archivo | ejemplo= 'data/A-n32-k5.vrp': ")
    num_iteraciones, ruta = validar_input(veces_a_aplicar, ruta_archivo)

    show_constants()
    # estado inicial
    if ruta is not None and ruta != "":
        capacity, nodes, optimal_idx = uselocalData(ruta)
    else:
        capacity, nodes, optimal_idx = downloadData()

    optimal_cost = optimals[optimal_idx]
    # Clientes y capacidad de camiones
    print_nodes(nodes)
    print("Capacidad de camiones: ", capacity)

    # Asignar funciones para aumentar velocidad
    funcion_recocido = SA.annealing
    funcion_costo = SA.costo_solucion
    gf = graph    

    print("\n---------------SOLUCION INICIAL---------------\n")

    initial_solution = SA.greedy_sol(nodes, capacity)
    costo_inicial = funcion_costo(initial_solution, nodes)
    print("Solucion inicial:", initial_solution)
    print("Costo solucion inicial:", costo_inicial)
    # live_plot(nodes, initial_solution)
    # draw_solution(nodes, initial_solution)

    gf.plt.ion()
    gf.plt.show()
    gf.plt.clf()
    gf.plot_solution(nodes, initial_solution)
    gf.plt.pause(1)

    print("\n---------------EJECUCION---------------\n")

    cost_sum = 0
    time_sum = 0
    max_cost = 0
    min_cost = 999999

    best_solution = initial_solution

    for i in range(num_iteraciones):
        # recocido simulado
        start_time = process_time()
        final_solution = funcion_recocido(
            nodes, capacity, previous_solution=best_solution)
        end_time = process_time()

        # tiempo y costo de iteracion
        time_diff = end_time - start_time
        costo_final = funcion_costo(final_solution, nodes)

        # mejor solucion
        if costo_final < min_cost:
            best_solution = final_solution

        # tiempo y costo acumulado
        time_sum += time_diff
        cost_sum += costo_final

        # estadisticas
        cost_diff_optimal = percent_diff(costo_final, optimal_cost)
        cost_diff_total = percent_diff(costo_inicial, costo_final)

        # mostrar datos
        max_cost = max(max_cost, costo_final)
        min_cost = min(min_cost, costo_final)
        print(f"\n ITERACION {i + 1} ")

        print("Solution final:", final_solution)
        print("Costo final:", costo_final)
        print(f"Costo {cost_diff_optimal:.2f} % MAYOR que el óptimo")

        print(f"Costo {cost_diff_total:.2f} % MENOR que el inicial")
        print(f"Tiempo de ejecución: {time_diff:.3f} segundos")

        gf.plt.clf()
        gf.plot_solution(nodes, best_solution)
        gf.plt.pause(0.1)

    # gf.draw_solution(nodes, final_solution)
    # end isinteractive
    if gf.plt.isinteractive():
        gf.plt.ioff()


if __name__ == "__main__":
    main()
    # TODO:
    # evitar que se cierre el ultimo grafico o volver a dibujarlo por ultimo
