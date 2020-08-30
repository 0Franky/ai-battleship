import numpy as np
from constants import *

# param: matrix = grafo da esplorare
# param: start = punto di partenza da cui iniziare l'esplorazione
# param: goal = funzione per determinare se un nodo è goal
# param: h = funzione di approssimazione
def iterative_deeping(matrix, start, goal):
    bound = 0 # limite
    path = np.array(start)
    while True:
        hit_depth_bound[0] = False
        res = depth_bounded_search(path, bound, matrix, hit_depth_bound, goal)
        if isArray(res):
            return res
        bound++
        if hit_depth_bound[0] == False:
            break
    return

    
# param: b = limite
# param: path = percorso
def depth_bounded_search(path, b, matrix, hit_depth_bound, goal):
    if (b > 0):
        for currentCouple in path:
            res = depth_bounded_search(path, b - 1, matrix, hit_depth_bound, goal)
            if isArray(res):
                return res
    else if goal(path[len(path) - 1]):
        return path
    else if hasNeighbor(matrix, path[len(path) - 1]):
        hit_depth_bound[0] = True
 
    
def isArray(val):
    return type(res) is np.ndarray

def hasNeighbor(matrix, cell):
    _hasNeighbor = False
    
    nextCell = matrix[cell[0] - 1][cell[1]]
    if nextCell == NOTHING or nextCell == FOOD:
        _hasNeighbor = True
        
    nextCell = matrix[cell[0] + 1][cell[1]]
    if nextCell == NOTHING or nextCell == FOOD:
        _hasNeighbor = True
        
    nextCell = matrix[cell[0]][cell[1] - 1]
    if nextCell == NOTHING or nextCell == FOOD:
        _hasNeighbor = True
        
    nextCell = matrix[cell[0]][cell[1] + 1]
    if nextCell == NOTHING or nextCell == FOOD:
        _hasNeighbor = True
        
    return _hasNeighbor