HULSKEN Alexandre & KARTI Adeniss

	SUDOKU SOLVER

Le solver a �t� enti�rement r�alis�.
Il est possible d'utiliser plusieurs extensions sous forme d'options au programme:
   * une option qui fait un affichage pas � pas
   * une option qui construit une image de l'arbre de r�solution
   * une option qui fait un calcul du co�t de r�cursion
   * une option qui construit une sous grille � celle donn�e avec moins de cellules d�finies tout en gardant une unique solution
   * un module graphique de solver qui poss�de toutes les options d�finies dans le module textuel avvec la possibilit� d'�crire une nouvelle grille � tout moment
   * un module graphique de jeu qui poss�de de nombreuses options (tel que la sauvegarde de la partie dans une fichier .grd, une extention cr�� pour l'occasion, un reset des cases remplies, l'ouverture d'un jeu enregistr� ou d'une grille de l'un des fichiers fournis en fonction du choix de difficult�, etc...)
   * un module de gestion total des modules graphiques

Les exemples possibles � utiliser pour le module textuel � partir du main sont:
* python3 main_projet.py -h
* python3 main_projet.py 495381267671245938382697154263578400814962375957134682738426500129853746546791823
* python3 main_projet.py 495381267671245938382697154263578491814962375957134682738416529129853746546729813 -rm
* python3 main_projet.py 000500420700100000300000000000038000040000050000070000150600000000000803000000002 -i lArbreTestRienQuePourVous -rec
* python3 main_projet.py 495381267671245938382697154263578400814962375957134682738426500129853746546791823 -i
* python3 main_projet.py 490001007000045030382600050003070401800902005907030600030006529020850000500700013 -t
* python3 main_projet.py 490001007000045030382600050003070401800902005907030600030006529020850000500700013 -rm -t
* python3 main_projet.py -gr
