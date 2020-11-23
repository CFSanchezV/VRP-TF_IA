# DATA
urlA = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/A/A-n32-k5.vrp"
ulrB = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/B/B-n31-k5.vrp"
ulrE = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/E/E-n101-k14.vrp"
urlX = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/X/X-n101-k25.vrp"
urls = [urlA, ulrB, ulrE, urlX]

rutas_locales = ['A-n32-k5.vrp', 'B-n31-k5.vrp', 'E-n101-k14.vrp', 'X-n101-k25.vrp']
# reference to url / file's optimal values
optimals = [784, 672, 1071, 27591]
optimals_dict = {'a': 784, 'b': 672, 'e': 1071, 'x': 27591}

# CONSTANTS
INITIAL_TEMP = 20
FINAL_TEMP = 1
T_FACTOR = 0.95


def show_constants():
    constdict = {
        "INITIAL_TEMP": INITIAL_TEMP,
        "FINAL_TEMP": FINAL_TEMP,
        "T_FACTOR": T_FACTOR
    }
    print("Parametros iniciales:")
    for k, v in constdict.items():
        print(k, v)


# utils

def percent_diff(a, b):
    return 100 * (a - b) / a


def print_nodes(nodes):
    print("Nodos (clientes):")
    for node in nodes:
        print(node)