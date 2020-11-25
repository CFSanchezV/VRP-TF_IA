# ONLINE DATASETS
# INITIAL urls
urlA = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/A/A-n32-k5.vrp"
ulrB = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/B/B-n31-k5.vrp"
ulrE = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/E/E-n101-k14.vrp"
urlX = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/X/X-n101-k25.vrp"

# EXTRA urls
urlA3 = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/A/A-n33-k6.vrp"
urlB3 = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/B/B-n35-k5.vrp"
urlE3 = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/E/E-n23-k3.vrp"
urlX3 = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/X/X-n110-k13.vrp"

urls = [urlA, ulrB, ulrE, urlX, urlA3, urlB3, urlE3, urlX3]

# LOCAL DATASETS
rutas_locales = ['A-n32-k5.vrp', 'B-n31-k5.vrp', 'E-n101-k14.vrp', 'X-n101-k25.vrp']

# reference to urls' / files' optimal values
optimals = [784, 672, 1071, 27591, 742, 955, 569, 14971]
optimals_dict = {'a': 784, 'b': 672, 'e': 1071, 'x': 27591, 'a3': 742, 'b3': 955, 'e3': 569, 'x3': 14971}

# CONSTANTS, need Tweaking
INITIAL_T = 20
T_FACTOR = 0.95
FINAL_TEMP = 1


def show_constants():
    constdict = {"TEMPERATURA_INICIAL": INITIAL_T, "TEMPERATURA_FINAL": FINAL_TEMP, "delta_T": T_FACTOR}
    print("Parámetros iniciales del algoritmo Simulated Annealing:")
    for key, val in constdict.items():
        print(key + ":", val)
    print("")


# UTILS 
def percent_diff(a, b):
    return 100 * (a - b) / a


def print_nodes(nodes):
    depot = nodes[0]
    print("Lista de clientes(Nodos):")
    print(f"Depósito id:{depot.id} con Demanda: {depot.demand} y Posición: ({depot.x}, {depot.y})")
    for node in nodes[1:]:
        print(node)


def set_xy_labels(ax1):
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')


def print_lista_rutas():
    for i, ruta in enumerate(rutas_locales):
        if i == len(rutas_locales)-1:
            print("'data/" + ruta + "'", end=' O DEJAR VACIO PARA DESCARGAR datos')
        else:
            print("'data/" + ruta + "'", end=', ')


def print_routes(all_routes):
    print("Rutas generadas según ID de Cliente(Nodo):")
    for i, route in enumerate(all_routes):
        print("Ruta", i+1, ":", route)
