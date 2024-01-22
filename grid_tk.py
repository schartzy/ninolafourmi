from tkinter import *
import grid_manager

# Dictionnaires des paramètres de forme d'une grille
COLORS = {'bg': 'white', 'fg': 'red', 'outline': 'black', 'text_val': 'black'}
FONT = {'text_val': 'Arial'}


def grid_canvas(master, grid, size_cell, margin=10, gutter=0, show_vals=False, outline=False):

    """Retourne un 'Canvas' placé dans la fenêtre 'master'. Celui-ci est construit à partir de la grille 'grid'
    en s'appuyant sur les modules 'grid_manager' et 'tkinter' ainsi que sur les dictionnaires des paramètres de forme.
    La largeur et la hauteur du Canvas sont calculés en considérant la taille 'size_cell' d'une cellule, la valeur de
    marge 'margin' autour de la grille et d'une taille de gouttière 'gutter' entre les lignes et les colonnes.
    Chaque cellule affichera en son centre le texte correspondant à son contenu si 'show_vals' est à la valeur 'True'.
    Les bordures des cellules ne s'afficheront que si 'outline' est à la valeur 'True'.
    Chaque cellule sera taguée par la chaine 'c_lin_col' et leur texte par la chaine 't_lin_col'.
    De plus, les deux seront taguées en plus par la chaine 'lin_col'."""

    num_lines = grid_manager.nb_lines(grid)
    num_cols = grid_manager.nb_columns(grid)

    canvas_width = num_cols * size_cell + (num_cols + 1) * gutter + 2 * margin
    canvas_height = num_lines * size_cell + (num_lines + 1) * gutter + 2 * margin

    canvas = Canvas(master, width=canvas_width, height=canvas_height, bg=COLORS['bg'])
    canvas.pack()

    rectangles_list = []

    for i in range(num_lines):
        for j in range(num_cols):
            x0 = margin + j * (size_cell + gutter)
            y0 = margin + i * (size_cell + gutter)
            x1 = x0 + size_cell
            y1 = y0 + size_cell

            rectangles_id = canvas.create_rectangle(x0, y0, x1, y1, outline=COLORS['outline'] if outline else "", fill='white', tags=[f"c_{i}_{j}", f"{i}_{j}"])
            canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(grid[i][j]) if show_vals else "", font=(FONT['text_val'], 10), fill=COLORS['text_val'], tags=[f"t_{i}_{j}", f"{i}_{j}"])
            rectangles_list.append(rectangles_id)
    return canvas, rectangles_list

def get_lines_columns(canvas):
    """Retourne le nombre de lignes et de colonnes de la grille représentée par le Canvas 'can'."""
    id_=canvas.find_all()[-1]
    tags=canvas.gettags(id_)[1]
    line,column=int(tags.split('_')[0])+1,int(tags.split('_')[1])+1
    return line,column


def get_grid(can):
    """Retourne la grille représentée par le Canvas 'can'."""

    grid = []
    num_rows, num_cols = get_lines_columns(can)
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            cell_value = get_cell_text(can, i, j)
            row.append(cell_value)
        grid.append(row)
    return grid


def get_color_cell(can, i, j):
    """Retourne la couleur de la cellule ('i', 'j') de la grille représentée par le Canvas 'can'."""
    tags = can.find_withtag(f"c_{i}_{j}")
    return can.itemcget(tags[0], "fill") if tags else None


def set_color_cell(can, i, j, color, outline=False):
    """Remplit la cellule ('i', 'j') de la grille représentée par le Canvas 'can' par la couleur 'color'.
    Dessine ses bordures avec la couleur 'color' si 'outline' a la valeur 'True'."""
    tags = can.find_withtag(f"c_{i}_{j}")
    if tags:
        can.itemconfigure(tags[0], fill=color)
        if outline:
            can.itemconfigure(tags[0], outline=color)

def get_color_text(can, i, j):
    """Retourne la couleur du texte de la cellule ('i', 'j') de la grille représentée par le Canvas 'can'."""
    tags = can.find_withtag(f"t_{i}_{j}")
    return can.itemcget(tags[0], "fill") if tags else None


def set_color_text(can, i, j, color):
    """Remplit le texte de la cellule ('i', 'j') de la grille représentée par le Canvas 'can' par la couleur 'color'."""
    tags = can.find_withtag(f"t_{i}_{j}")
    if tags:
        can.itemconfigure(tags[0], fill=color)


def get_cell_text(can, i, j):
    """Retourne la valeur du texte de la cellule ('i', 'j') du Canvas 'can'"""
    tags = can.find_withtag(f"t_{i}_{j}")
    print(tags)
    return can.itemcget(tags[0], "text") if tags else None


def set_cell_text(can, i, j, val):
    """Change la valeur du texte de la cellule ('i', 'j') du Canvas 'can' avec la valeur 'val'"""
    
    tags = can.find_withtag(f"t_{i}_{j}")
    if tags:
        can.itemconfigure(tags[0], text=val)


def set_cell(can, grid, i, j, val, color_cell, show_vals=False, outline=True, color_text=COLORS['text_val']):
    """Modifie la grille 'grid' et le Canvas 'can' en affectant la valeur 'val' à la cellule ('i', 'j').
    Change la couleur de fond par 'color_cell'.
    Change la couleur du texte par 'color_text' et la valeur par 'val' si 'show_vals' a la valeur 'True'.
    Dessine les bordures de la cellule selon la valeur booléenne de 'outline'."""
    set_color_cell(can, i, j, color_cell, outline)
    if show_vals:
        set_cell_text(can, i, j, val)
        set_color_text(can, i, j, color_text)

def update_canvas(canva, grid,color):
    """Met à jour la grille actuelle sur le Canvas."""
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==1:
                set_cell(canva, grid, i, j, grid[i][j], color, outline=True)
    return canva


