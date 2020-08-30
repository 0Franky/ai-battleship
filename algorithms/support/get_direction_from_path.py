from snake import *
import numpy as np

def get_direction_from_path(start, direction, next_hop):
    next_direction = [0, 0, 0]
    if direction == RIGHT:
        y_sub = next_hop[1] - start[1]
        if (x_sub > 0):
            next_direction = [0, 0, 1]
        else:
            next_direction = [0, 1, 0]
            
    if direction == LEFT:
        y_sub = next_hop[1] - start[1]
        if (x_sub > 0):
            next_direction = [0, 1, 0]
        else:
            next_direction = [0, 0, 1]
            
    if direction == UP:
        x_sub = next_hop[0] - start[0]
        if (x_sub > 0):
            next_direction = [0, 1, 0]
        else:
            next_direction = [0, 0, 1]
            
    if direction == DOWN:
        x_sub = next_hop[0] - start[0]
        if (x_sub > 0):
            next_direction = [0, 0, 1]
        else:
            next_direction = [0, 1, 0]
            
    decision = np.argmax(next_direction)
    if decision == 1:
        snake.turn_right()
    elif decision == 2:
        snake.turn_left()
    # return next_direction