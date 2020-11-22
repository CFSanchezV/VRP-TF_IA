# DATA
urlA = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/A/A-n32-k5.vrp"
ulrB = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/B/B-n31-k5.vrp"
ulrE = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/E/E-n101-k14.vrp"
urlX = "http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/X/X-n101-k25.vrp"
urls = [urlA, ulrB, ulrE, urlX]

# idx: reference to url / file's optimal values
optimals = [784, 672, 1071, 27591]

# CONSTANTS
INITIAL_TEMP = 100
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
