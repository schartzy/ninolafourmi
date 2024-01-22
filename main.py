from tkinter import *
from tkinter import ttk
import grid_manager
import grid_tk
from fourmi_langton import *
from fenetre__du_jeu import *

cell_size = 5
cell_size_2 = 10
grille_cree = False
selected_value = 'black'
own_grid = grid_manager.create_grid_lc(20, 20, 0)

def fonction_bouton_simulation():
    fenêtre_simulation(root, "Fourmi de Langton", grid_manager.create_grid_lc(100, 100, 0), cell_size)

def fonction_bouton_deux():
    fenêtre_simulation(root, "Fourmi de Langton", own_grid, cell_size_2, selected_value)

def fonction_simulation2():
    fenêtre_simulation(root, "Fourmi de Langton", grid_manager.create_random_grid_2(100, 20, [0,1]), cell_size)

root = Tk()
root.title("Page d'Accueil")

largeur_fenetre = 700
hauteur_fenetre = 520
dimensions_fenetre = f"{largeur_fenetre}x{hauteur_fenetre}"
root.geometry(dimensions_fenetre)

global grid_size_2
grid_size_2 = 20

def on_select(event):
    global selected_value
    selected_value = couleur_var.get()

def size_grid(selected_size):
    global grid_size_2, own_grid
    grid_size_2 = selected_size
    grid_size_2 = int(grid_size_2)
    own_grid = grid_manager.create_grid_lc(grid_size_2, grid_size_2, 0)
def open_grid_window():
    def toggle_color(event):
        global liste_modifié
        liste_modifié = own_grid
        clicked_rect = event.widget.find_closest(event.x, event.y)
        current_color = event.widget.itemcget(clicked_rect, "fill")
        x, y = (event.x - 10)// cell_size_2, (event.y - 10 )// cell_size_2
        if current_color == "white":
            event.widget.itemconfig(clicked_rect, fill=selected_value)
            own_grid[y][x] = 1
        else:
            event.widget.itemconfig(clicked_rect, fill="white")
            own_grid[y][x] = 0
        return liste_modifié

    def save_grid():
        own_grid = liste_modifié
        interactif.destroy()
        return own_grid
    
    def reset_grid():
        global own_grid
        own_grid = grid_manager.create_grid_lc(grid_size_2, grid_size_2, 0)

        for rect_id in rectangles_list:
            own_canvas.itemconfig(rect_id, fill="white")

        return own_grid
    
    global own_grid, grid_size_2, grille_cree
    if grille_cree == False:
        own_grid = grid_manager.create_grid_lc(grid_size_2, grid_size_2, 0)
        grille_cree = True
    elif grille_cree == True and grid_size_2 != len(own_grid):
        own_grid = grid_manager.create_grid_lc(grid_size_2, grid_size_2, 0)


    interactif = Toplevel()
    interactif.title("Création de la grille interactive")
    interactif.grab_set()

    global own_canvas, rectangles_list
    own_canvas, rectangles_list = grid_tk.grid_canvas(interactif, own_grid, cell_size_2, outline=True)
    own_canvas.pack(pady=10)

    grid_tk.update_canvas(own_canvas, own_grid, selected_value)

    for rect_id in rectangles_list:
        own_canvas.tag_bind(rect_id, "<Button-1>", toggle_color)

    save_button = Button(interactif, text="Enregistrer la grille", command=save_grid)
    save_button.pack(side=RIGHT, padx=10, pady=10)

    save_button = Button(interactif, text="Réinitialiser la grille", command=reset_grid)
    save_button.pack(side=LEFT, padx=10, pady=10)

    interactif.resizable(height = 0, width = 0)
    interactif.mainloop()


titre_principal = Label(root, text="La Fourmi de Langton", font=("Arial", 20, "bold"))
titre_principal.pack(pady=10)

texte_explicatif = """On nomme fourmi de Langton un automate cellulaire bidimensionnel comportant un jeu avec des règles très simples. On lui a donné le nom de Christopher Langton, son inventeur. Les cases d'une grille bidimensionnelle peuvent être blanches ou noires. On considère arbitrairement l'une de ces cases comme étant l'emplacement initial de la fourmi. Dans l'état initial, toutes les cases sont de la même couleur.
La fourmi peut se déplacer à gauche, à droite, en haut ou en bas d'une case à chaque fois selon les règles suivantes :
Si la fourmi est sur une case noire, elle tourne de 90° vers la gauche, change la couleur de la case en blanc et avance d'une case.
Si la fourmi est sur une case blanche, elle tourne de 90° vers la droite, change la couleur de la case en noir et avance d'une case.
Ces règles simples conduisent à un comportement étonnant de la fourmi : après une période initiale apparemment chaotique, la fourmi finit par construire une « autoroute » formée par 104 étapes qui se répètent indéfiniment."""
label_explicatif = Label(root, text=texte_explicatif, bg='lavender', justify=LEFT, wraplength=600)
label_explicatif.pack(padx=20, pady=10)

frame_ligne_0 = Frame(root)
frame_ligne_0.pack(fill=X, padx=20, pady=(0, 10))

frame_ligne_1 = Frame(root)
frame_ligne_1.pack(fill=X, padx=20, pady=(0, 10))

frame_ligne_2 = Frame(root)
frame_ligne_2.pack(fill=X, padx=20, pady=(0, 10))

frame_ligne_3 = Frame(root)
frame_ligne_3.pack(fill=X, padx=20, pady=(0, 10))

frame_ligne_4 = Frame(root)
frame_ligne_4.pack(fill=X, padx=20, pady=(0, 10))

frame_ligne_5 = Frame(root)
frame_ligne_5.pack(fill=X, padx=20, pady=(0, 10))

titre_option1 = Label(frame_ligne_0, text="Test de la Fourmi de Langton", font=("Arial", 12, "bold"))
titre_option1.pack()

bouton_simulation = Button(frame_ligne_1, text="Simulation sur une grille vierge", command=fonction_bouton_simulation)
bouton_simulation.pack(side=LEFT, padx=50)

bouton_simulation2 = Button(frame_ligne_1, text="Simulation avec une disposition aléatoire", command=fonction_simulation2)
bouton_simulation2.pack(side=RIGHT, padx=50)

t_simulation = Label(frame_ligne_2,text="Personnalisation de la simulation", font=("Arial", 12, "bold"))
t_simulation.pack()

t_simulation = Label(frame_ligne_3, text="Choix de la couleur de la trace", font=("Arial", 8, "bold"))
t_simulation.pack(side=LEFT)

t_simulation = Label(frame_ligne_3, text="Choix de la taille de la grille", font=("Arial", 8, "bold"))
t_simulation.pack(side=LEFT, padx=73)

t_simulation = Label(frame_ligne_3, text="Choix de la disposition de départ", font=("Arial", 8, "bold"))
t_simulation.pack(side=RIGHT)

couleurs = ["black", "Red", "Blue", "green", "yellow", "Orange", "pink", "Violet"]
selected_color = StringVar()
couleur_var = ttk.Combobox(frame_ligne_4, values=couleurs, textvariable=selected_color, state="readonly", height=4)
couleur_var.pack(side = LEFT, padx=10)
couleur_var.bind("<<ComboboxSelected>>", on_select)
selected_color.set(couleurs[0])

speed_scale = Scale(frame_ligne_4, from_=20, to=70, orient=HORIZONTAL, command=size_grid)
speed_scale.pack(side=LEFT, padx=100)

bouton_grille = Button(frame_ligne_4, text="Ouvrir la grille", command=open_grid_window)
bouton_grille.pack(side=RIGHT, padx=30)

bouton_deux = Button(frame_ligne_5, text="Lancer la simulation", command=fonction_bouton_deux)
bouton_deux.pack()

bouton_close = Button(frame_ligne_5, text="Fermer", command=root.destroy)
bouton_close.pack(side=RIGHT)


root.resizable(height = 0, width = 0)
root.mainloop()