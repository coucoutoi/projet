HULSKEN Alexandre & KARTI Adeniss

	SUDOKU SOLVER

Le solver a été entièrement réalisé.
Il est possible d'utiliser plusieurs extensions sous forme d'options au programme:
   * une option qui fait un affichage pas à pas
   * une option qui construit une image de l'arbre de résolution
   * une option qui fait un calcul du coût de récursion
   * une option qui construit une sous grille à celle donnée avec moins de cellules définies tout en gardant une unique solution
   * un module graphique de solver qui possède toutes les options définies dans le module textuel avvec la possibilité d'écrire une nouvelle grille à tout moment
   * un module graphique de jeu qui possède de nombreuses options (tel que la sauvegarde de la partie dans une fichier .grd, une extention créé pour l'occasion, un reset des cases remplies, l'ouverture d'un jeu enregistré ou d'une grille de l'un des fichiers fournis en fonction du choix de difficulté, etc...)
   * un module de gestion total des modules graphiques

Les exemples possibles à utiliser pour le module textuel à partir du main sont:
* python3 main_projet.py -h
* python3 main_projet.py 495381267671245938382697154263578400814962375957134682738426500129853746546791823
* python3 main_projet.py 495381267671245938382697154263578491814962375957134682738416529129853746546729813 -rm
* python3 main_projet.py 000500420700100000300000000000038000040000050000070000150600000000000803000000002 -i lArbreTestRienQuePourVous -rec
* python3 main_projet.py 495381267671245938382697154263578400814962375957134682738426500129853746546791823 -i
* python3 main_projet.py 490001007000045030382600050003070401800902005907030600030006529020850000500700013 -t
* python3 main_projet.py 490001007000045030382600050003070401800902005907030600030006529020850000500700013 -rm -t
* python3 main_projet.py -gr
