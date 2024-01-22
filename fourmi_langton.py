from tkinter import *
import grid_manager
import grid_tk

def langton_ant(canvas, grid, pos_x_fourmi, pos_y_fourmi, direction, color='black'):
    dir_haut = 0
    dir_droite = 1
    dir_bas = 2
    dir_gauche = 3
    
    current_color = grid_tk.get_color_cell(canvas,pos_x_fourmi,pos_y_fourmi)

    if current_color == 'white':
        grid_tk.set_cell(canvas, grid, pos_x_fourmi, pos_y_fourmi, 1, color, outline=True)
        direction = (direction + 1) % 4
    else:
        grid_tk.set_cell(canvas, grid, pos_x_fourmi, pos_y_fourmi, 0, 'white', outline=True)
        direction = (direction - 1) % 4
    
    if direction == dir_haut:
        pos_x_fourmi -= 1
    elif direction == dir_droite:
        pos_y_fourmi += 1
    elif direction == dir_bas:
        pos_x_fourmi += 1
    elif direction == dir_gauche:
        pos_y_fourmi -= 1

    grid_size = len(grid)
    pos_x_fourmi %= grid_size
    pos_y_fourmi %= grid_size

    return canvas, grid, pos_x_fourmi, pos_y_fourmi, direction