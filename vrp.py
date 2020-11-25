from time import process_time
from math import inf as infinito
from constants import show_constants, rutas_locales, percent_diff, print_nodes, print_lista_rutas, set_xy_labels, print_routes
from initialSolution import downloadData, uselocalData, optimals, get_solution_routes
import graph
import simulatedAnnealing as SA


def validar_input(veces_a_aplicar, ruta_archivo):
    try:
        veces = int(veces_a_aplicar)
        ruta = str(ruta_archivo)
    except ValueError:
        print("Número de iteraciones inválido")
        exit()

    if ruta == "":
        print("\nRuta vacía, descargando datos aleatorios de CVRPLIB, URL: http://vrp.atd-lab.inf.puc-rio.br/index.php/en/\n")
    return veces, ruta


def main():
    print("\nNOTA: Se recomienda aumentar el tamaño de la consola para visualizar mejor los datos durante y al final de la ejecución del programa")
    print("---------------INICIALIZACIÓN---------------\n")    
    print("Se recomienda un MÍNIMO de 20 y un MÁXIMO de 200, puede tardar algunos minutos con datasets grandes. Los 2 primeros datasets locales (A y B) son los más pequeños")
    veces_a_aplicar = input("Ingresar número de iteraciones: ")
    print("\nArchivos locales: ", end='')
    print_lista_rutas()

    ruta_archivo = input("\nIngresar ruta de archivo, por ejemplo:'data/A-n32-k5.vrp', (opcional): ")
    num_iteraciones, ruta = validar_input(veces_a_aplicar, ruta_archivo)

    show_constants()
    # estado inicial
    if ruta is not None and ruta != "":
        capacity, nodes, optimal_idx = uselocalData(ruta)
    else:
        capacity, nodes, optimal_idx = downloadData()

    optimal_cost = optimals[optimal_idx]
    
    # Clientes y capacidad de camiones
    print("--------Datos del dataset--------")    
    print_nodes(nodes)
    print("\nCapacidad de camiones: ", capacity)
    
    print("\n^^Arriba se muestran los datos del dataset elegido/descargado^^")
    lil_break = input("-------Presione ENTER para continuar-------")

    # Asignar funciones para aumentar velocidad
    funcion_recocido = SA.annealing
    funcion_costo = SA.costo_solucion
    gf = graph

    print("\n---------------SOLUCIÓN INICIAL---------------\n")

    initial_solution = SA.greedy_sol(nodes, capacity)
    costo_inicial = funcion_costo(initial_solution, nodes)
    print("Solución inicial:", initial_solution)
    print("Costo solución inicial:", costo_inicial)

    # gf.live_plot(nodes, initial_solution)

    # subplots' axis + plotting
    fig, (ax1, ax2) = gf.plt.subplots(nrows=1, ncols=2, figsize=(12, 5), tight_layout=True)
    fig.canvas.set_window_title('Enrutamiento de vehiculos')
    
    gf.live_subplot(nodes, initial_solution, ax1, "Primera Solución")    

    print("\n---------------EJECUCIÓN DE ALGORITMO SA---------------\n")

    cost_sum = 0
    time_sum = 0    
    min_cost = infinito

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
        min_cost = min(min_cost, costo_final)
        # max_cost?

        # mostrar datos        
        print("\n ITERACION", i + 1)

        print("Solución final:", final_solution)
        print("Costo final:", costo_final)
        print(f"Costo {cost_diff_optimal:.2f}% MAYOR al óptimo")

        print(f"Costo {cost_diff_total:.2f}% MENOR al inicial")
        print(f"Tiempo de ejecución: {time_diff:.3f} segundos")

        # gf.live_plot(nodes, best_solution)  # single graph

        # subplots' axis + plotting
        gf.live_subplot(nodes, best_solution, ax2, "Solución Actual")

    # end isinteractive
    if gf.plt.isinteractive():
        gf.plt.ioff()
        gf.plt.close(fig)
    
    print("\n----FIN DE EJECUCIÓN^^----\n")    


    # -------------------MOSTRAR RESUMEN DE RESULTADO OBTENIDO---------------
    print("\n----RESUMEN Y ANÁLISIS DE EJECUCIÓN:----\n")  

    average_cost = int(cost_sum / num_iteraciones)
    average_time = time_sum / num_iteraciones

    print(f"{num_iteraciones} ejecuciones del algoritmo en: {time_sum:.3f} segundos")
    print(f"Tiempo promedio de ejecución: {average_time:.3f} segundos\n")
    print("Costo óptimo conocido: ", optimal_cost)
    print("Costo solución final: ", costo_final)
    print("Costo inicial: ", costo_inicial)
    print(f"Mejor costo hallado es {cost_diff_optimal:.2f}% MAYOR al óptimo (PEOR)")
    print("Costo promedio:", average_cost, "\n")    
    # Mostrar Rutas
    rutas_en_solucion = get_solution_routes(best_solution)
    print_routes(rutas_en_solucion)


    # Graficar solución final
    gf.draw_solution(nodes, best_solution)


if __name__ == "__main__":
    main()
    # TODO:
    # obtener estadisticas para tablas y comparaciones---
