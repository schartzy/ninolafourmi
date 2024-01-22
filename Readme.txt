Projet Langton, Conception de logiciel 
MIASHS L3 2023/2024

PIGEON Thomas
ROGER Armand

	Manuel d'utilisation du programme:
Le jeu possède une page d'accueil qui explique brièvement comment fonctionne la fourmi de Langton, puis nous avons une partie interactive divisé en 2 parties.
1ER Partie: Test de la fourmi de Langton
Nous avons ici 2 boutons qui permettent tous les deux de lancer une simulation de la fourmi de langton dans une autre fenêtre. La fenêtre qui apparaît possède un canva où est disposé la 
grille où évolue la simulation. En dessous il y a un slider pour augmenter le délais entre chaque géneration, un bouton pour démarrer qui permet ensuite de mettre en pause et reprendre la 
simulation, un compteur de géneration et un bouton pour fermer la fenêtre. Le bouton "Simulation sur une grille vierge" ouvre la fenêtre de simulation avec une grille blanche tandis que le 
bouton "Simulation avec une disposition aléatoire" ouvre la fenêtre avec une grille blanche mais une disposition aléatoire de case noir et blanche au centre de la grille (car une grille 
complètement aléatoire ne ferait pas apparaître l'autoroute).

2EME Partie: Personnalisation de la simulation
Nous avons ici 3 widgets, le menu déroulant "ComboBox" permet de choisir une couleur différente de noir pour la trace, elle sera noir par défaut. Ensuite un slider qui permet de choisir la 
taille de la grille, elle sera de 20x20 par défaut. Et un bouton qui ouvre une fenêtre permettant de choisir la disposition de départ de la grille. Cette fenêtre dispose du canva avec une 
grille blanche où il suffit de cliquer sur la case que l'on souhaite colorer ou redéfinir en blanc, en dessous du canva un bouton qui réinitialise la grille en blanc et un bouton pour 
enregistrer la grille créé.
Ensuite en bas nous avons le bouton "Lancer la simulation" qui ouvre la fenêtre qui permet de simuler la fourmi comme dans la partie 1. Par défaut ce sera donc une grille blanche 20x20 
avec une couleur de la trace en noir.

Puis en bas a droite un bouton "Fermer" qui quitte la jeu.
Les fenêtres ne sont pas redimensionnable, pour ne pas déplacer la manière dont son packés les widgets. Et la fenêtre d'accueil n'est pas utilisable lorsqu'une fenêtre tierce est ouverte 
pour éviter les erreurs avec les modifications de variable.



	Fonctionnalité rajouté a la fourmi de Langton:
-Page d'accueil interactif
-Grille avec une disposition aléatoire de départ
-Possibilité de créer sa propre grille avec une autre couleur que noir, une taille de grille au choix et une disposition de case coloré de départ au choix.
-Il est possible pendant la simulation de régler le délais entre chaque géneration, de mettre en pause et de reprendre la simulation et il y a un compteur du nombre de géneration.


	Choix d'implémentation:
Il y a 5 fichiers,
Le fichier grid_manager qui permet de créer et d'obtenir des informations sur des grilles;
Le fichier grid_tk qui permet de créer une grille sur un canva associé à la grille donnée et d'obtenir et modifier ses cases;
Le fichier fourmi_langton qui fait évoluer la fourmi dans le canva;
Le fichier fenetre_du_jeu qui créer la fenêtre ou le canva est affiché et où les boutons pour interagir avec la simulation sont créé;
Le fichier main qui est à executer qui créer la fenêtre d'accueil du jeu et sauvegarde les variables choisi pour la personnalisation de la simulation

Le fichier main contient les fonctions des boutons qui appel le fichier fenêtre_du_jeu pour ouvrir les fenêtre de simulation et qui utilise le fichier fourmi_langton pour la simulation 
sur le canva. Il contient les informations pour créer la fenêtre d'accueil et les fonctions pour modifier les valeurs de personnalisation, ensuite nous avons la création des frames et des 
widgets pour la fenêtre.


	Partie de code créé par IA:
Les fichiers grid_manager et grid_tk ont été rempli par IA et modifié si ils ne fonctionnaient pas. Exepté pour les fonctions rajoutés par nous dans ces deux fichiers.
Le menu déroulant utilisant ttk a été créé par IA
La création de la fenêtre et le code pour avoir une grille intéractive lorsque l'on clique sur une case à été généré par IA puis légèrement modifié car ne fonctionnait pas dans notre 
fichier


	Répartition du travail:
La fonction langton_ant ainsi que le fichier fenetre_du_jeu à été codé par nous deux
La fenêtre d'accueil a été codé par Armand ROGER
Les boutons et fonction associé à la couleur de la trace, taille de la grille et la grille interactive ont été ajouté par Thomas PIGEON





