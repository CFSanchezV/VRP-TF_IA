from math import sqrt

class Node:
    """ Node class / Clients """
    
    def __init__(self, id, demand, x, y):
        """
        param id: identifier
        param demand: client demand(int)
        param x: starting x pos (int)
        param y: starting y pos (int)
        """
        self.id = id
        self.demand = int(demand)
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"Cliente {self.id} con Demanda: {self.demand} y Posición: ({self.x}, {self.y})"

    # Comparator True | False eq
    def __eq__(self, other):
        return self.id == other.id

    def distance_to_node(self, x, y):
        # return int
        return round(sqrt((self.x - x)**2 + (self.y - y)**2))


class Route:
    """ Route class """
    
    def __init__(self, path, cost=0):
        """
        param path: list
        param cost: dist travelled
        """
        self.path = path
        self.cost = cost

    def __repr__(self):
        return f"Ruta | Costo: {self.cost}, Camino: {self.path}"
