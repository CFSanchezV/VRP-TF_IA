# ANNEALING CONSTANTS ####

INITIAL_TEMP = 100
FINAL_TEMP = 1
T_FACTOR = 0.95

def show_constants():
    const = {
        "INITIAL_TEMP": INITIAL_TEMP,
        "FINAL_TEMP": FINAL_TEMP,
        "T_FACTOR": T_FACTOR
    }
    print("Constants:")
    for k, v in const.items():
        print(k, v)    
    print("\n")
