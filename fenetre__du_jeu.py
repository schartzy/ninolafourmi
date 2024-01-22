from tkinter import *
from tkinter import ttk
import grid_manager
import grid_tk
from fourmi_langton import *

def fenêtre_simulation(root, title, initial_grid, cell_size_val, couleur='black'):
    simulation_window = Toplevel(root)
    simulation_window.title(title)
    simulation_window.grab_set()

    global run, speed, canvas, grid, pos_x_fourmi, pos_y_fourmi, direction, generation
    run = False
    speed = 1
    generation = 0

    grid = initial_grid
    pos_x_fourmi = len(grid) // 2
    pos_y_fourmi = len(grid[0]) // 2
    direction = 0

    canvas = grid_tk.grid_canvas(simulation_window, grid, cell_size_val)
    canvas = canvas[0]
    grid_tk.update_canvas(canvas, grid, couleur)
    canvas.pack

    def simulation():
        global generation
        generation += 1
        global id_jeu, canvas, grid, pos_x_fourmi, pos_y_fourmi, direction
        canvas, grid, pos_x_fourmi, pos_y_fourmi, direction = langton_ant(canvas, grid, pos_x_fourmi, pos_y_fourmi, direction, color=couleur)
        label_generation.config(text=f"Générations: {generation}")
        id_jeu = canvas.after(speed, simulation)
        return canvas

    def stop_simulation():
        canvas.after_cancel(id_jeu)

    def start_pause():
        global run
        if not run:
            b_start_pause['text'] = '    Pause    '
            run = True
            simulation()
        else:
            b_start_pause['text'] = 'Reprendre'
            run = False
            stop_simulation()

    def set_speed(new_speed):
        global speed
        speed = new_speed

    speed_scale = Scale(simulation_window, from_=1, to=100, orient=HORIZONTAL, label="Délai en ms", command=set_speed)
    speed_scale.pack(side=LEFT, padx=5)

    b_start_pause = Button(simulation_window, text="Démarrer", command=start_pause)
    b_start_pause.pack(side=LEFT, padx=50)

    label_generation = Label(simulation_window, text="Génération : 0", font=("Arial", 12, "bold"))
    label_generation.pack(side=LEFT, padx=5)

    close_button = Button(simulation_window, text="Fermer", command=simulation_window.destroy)
    close_button.pack(side=RIGHT, padx=15)

    simulation_window.resizable(height=0, width=0)
    simulation_window.mainloop()

