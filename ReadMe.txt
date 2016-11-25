Pour pouvoir utiliser et lancer votre sudoku solver, vous pouvez utiliser les 2 modes diff�rentes:
	# LE MODE TEXTUEL #
		1�re m�thode -> lancez un terminal et lancer le fichier main_solver.py suivi de la grille sous forme d'une suite de nombre avec des 0 pour symboliser une case vide (pour avoir plus d'informations sur les diff�rentes options disponible de votre solver, lancer le fichier suivi de -h ou --help pour appliquer la fonction d'aide)
		2nde m�thode -> ouvrez le fichier sudoku_solver.py dans un terminal idle puis lancez le programme, il vous suffira ensuite de cr�er une grille avec la fonction make_grid du module sudoku_grid (celui-ci est d�j� import�, utiliser une ligne de code sous cette forme: >>> gird = sudoku_grid.make_grid(string) o� string correspond � votre cha�ne de caract�re repr�sentant la grille) et de lui apliquer la fonction search_sol (vous pourrez alors utiliser cette ligne de code: >>> search_sol(grid))

	# LE MODE GRAPHIQUE #
		1�re m�thode -> lancez un terminal et lancer le fichier main_solver.py suivi seulement de l'option -gr (ou --graphical) puis vous pourez utiliser votre solver
		2nde m�thode -> ouvrez le fichier graphical.py dans un terminal idle puis lancez le programme, il vous suffira ensuite appeler la fonction create et vous pourrez utiliser votre solver

Information suppl�mentaire: l'option graphique du solver ne fonctionne pas lorsque vous utilisez la premi�re m�thode donn�e