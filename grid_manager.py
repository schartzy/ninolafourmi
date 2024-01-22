import random

def create_grid_lc(lin, col, val):
    """Retourne une grille de 'lin' lignes et 'col' colonnes
    initialisées à 'val'"""
    return [[val] * col for _ in range(lin)]

def create_random_grid_lc(lin, col, vals):
    """Retourne une grille de 'lin' lignes et 'col' colonnes
    initialisés aléatoirement avec des valeurs de la liste 'vals'"""
    return [[random.choice(vals) for _ in range(col)] for _ in range(lin)]

def nb_lines(grid):
    """Retourne le nombre de lignes de la grille 'grid'"""
    return len(grid)

def nb_columns(grid):
    """Retourne le nombre de colonnes de la grille 'grid'"""
    return len(grid[0]) if grid else 0

def line2str(grid, num_line, sep='\t'):
    """Retourne la chaine de caractère correspondant à la concaténation des valeurs
    de la ligne numéro 'num_line' de la grille 'grid'. Les caractères sont séparés par le caractère 'sep'"""
    return sep.join(map(str, grid[num_line]))

def grid2str(grid, sep='\t'):
    """Retourne la chaine de caractère représentant la grille 'grid'.
    Les caractères de chaque ligne de 'grid' sont séparés par le caractère 'sep'.
    Les lignes sont séparées par le caractère de retour à la ligne \n"""
    return '\n'.join(line2str(grid, i, sep) for i in range(nb_lines(grid)))

def neighbour(grid, lin, col, delta, tore=True):
    """Retourne le voisin de la cellule 'grid[lin][col]' selon le tuple 'delta' = (delta_lin, delta_col).
    Si 'tore' est à 'True' le voisin existe toujours en considérant 'grid' comme un tore.
    Si 'tore' est à 'False' retourne 'None' lorsque le voisin est hors de la grille 'grid'."""
    n_lin, n_col = lin + delta[0], col + delta[1]
    if tore:
        n_lin %= nb_lines(grid)
        n_col %= nb_columns(grid)
    return grid[n_lin][n_col] if 0 <= n_lin < nb_lines(grid) and 0 <= n_col < nb_columns(grid) else (None if not tore else grid[n_lin % nb_lines(grid)][n_col % nb_columns(grid)])

def neighborhood(grid, lin, col, deltas, tore=True):
    """Retourne pour la grille 'grid' la liste des N voisins de 'grid[lin][col]'
    correspondant aux N (delta_lin, delta_col) fournis par la liste 'deltas'.
    Si 'tore' est à 'True' le voisin existe toujours en considérant 'grid' comme un tore.
    Si 'tore' est à 'False' un voisin hors de la grille 'grid' n'est pas considéré."""
    return [neighbour(grid, lin, col, delta, tore) for delta in deltas]

def create_random_grid_2(size1, size2, vals):
    grid = create_grid_lc(size1, size1, vals[0])
    for i in range((size1//2)-(size2//2), (size1//2)+(size2//2)):
        for j in range((size1//2)-(size2//2), (size1//2)+(size2//2)):
            grid[i][j]=random.choice(vals)
    return grid

if __name__ =="__main__":
    grid = create_random_grid_2(10,5,[0,1])
    print(grid)


