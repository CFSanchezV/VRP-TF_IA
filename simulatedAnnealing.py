from constants import T_FACTOR, INITIAL_T, FINAL_TEMP
from initialSolution import greedy_sol, rnd
from copy import deepcopy
import math


# intercambiar dentro de solucion
def intercambiar(solution_input):
    # deepcopy, recrear Nodos en lista ref tambien
    solution = deepcopy(solution_input)
    last_pos = len(solution_input) - 2

    i = rnd.randint(1, last_pos)
    j = rnd.randint(1, last_pos)

    # intercambio de indices
    solution[i], solution[j] = solution_input[j], solution_input[i]

    return solution


# Mover a indice aleatorio
def mover(solution_input):
    last_pos = len(solution_input) - 2
    i = rnd.randint(1, last_pos)
    j = rnd.randint(1, last_pos)

    # minimo: i, maximo: j
    i, j = min(i, j), max(i, j)

    # Mover de indice i a indice j
    return solution_input[:i] + solution_input[i + 1:j] + [solution_input[i]] + solution_input[j:]


# Invertir seccion
def invertir(solution_input):
    last_pos = len(solution_input) - 2
    i = rnd.randint(1, last_pos)
    j = rnd.randint(1, last_pos)

    # minimo: i, maximo: j
    i, j = min(i, j), max(i, j)

    # Invertir de indice i a indice j
    return solution_input[:i] + solution_input[i:j][::-1] + solution_input[j:]


def generar_vecino(solution_input):
    operaciones = [intercambiar, mover, invertir]
    operacion = rnd.choice(operaciones)
    return operacion(solution_input)


def solucion_es_valida(solution, nodes, capacity):
    end = start = 0
    while end < len(solution):
        start = end

        end = start + solution[start:].index(0) + 1
        route = solution[start:end]

        sum_demand_route = sum(
            [nodes[client_id].demand for client_id in route])
        if sum_demand_route > capacity:
            return False

    return True


def acepta_nuevo_vecino(delta, T):
    prob = math.exp(-delta / T)
    return rnd.random() < prob


def costo_solucion(solution_input, nodes):
    cost = 0
    node = nodes[solution_input[0]]

    for sol in solution_input[1:]:
        adj_node = nodes[sol]
        cost += node.distance_to_node(adj_node.x, adj_node.y)
        node = adj_node

    return cost


def annealing(nodes, capacity, init_t=INITIAL_T, t_factor=T_FACTOR, previous_solution=None):
    if previous_solution is None:
        previous_solution = greedy_sol(nodes, capacity)

    mejor_sol = sol_actual = previous_solution
    mejor_costo = costo_actual = costo_solucion(sol_actual, nodes)

    T = init_t
    N = int(len(nodes)*0.9)

    while T > FINAL_TEMP:
        i = 0

        while i < N:
            # primer estado alterado
            nueva_sol = generar_vecino(sol_actual)
            # solucion no valida
            if not solucion_es_valida(nueva_sol, nodes, capacity):
                continue

            # calcular deltaC
            nuevo_costo = costo_solucion(nueva_sol, nodes)
            deltaC = nuevo_costo - costo_actual

            if deltaC < 0:  # mejor solcion
                sol_actual = nueva_sol
                costo_actual = nuevo_costo
                if nuevo_costo < mejor_costo:  # es mejor solucion
                    mejor_sol = nueva_sol
                    mejor_costo = nuevo_costo

            # peor solucion: probabilidad math.exp(-delta/T)
            elif acepta_nuevo_vecino(deltaC, T):
                sol_actual = nueva_sol
                costo_actual = nuevo_costo

            i += 1
        # ajustar temperatura
        T = T*t_factor
        # print(T)  # show Temp

    return mejor_sol
