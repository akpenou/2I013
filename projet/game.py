# coding: utf-8
from copy import deepcopy
# plateau: List[List[nat]]
# liste de listes (lignes du plateau) d'entiers correspondant aux contenus des cases du plateau de jeu

# coup: Pair[nat nat]
# Numero de ligne et numero de colonne de la case correspondante a un coup d'un joueur

# Jeu
# jeu:N-UPLET[plateau nat List[coup] List[coup] Pair[nat nat]]
# Structure de jeu comportant :
#           - le plateau de jeu
#           - Le joueur a qui c'est le tour de jouer (1 ou 2)
#           - La liste des coups possibles pour le joueur a qui c'est le tour de jouer
#           - La liste des coups joues jusqu'a present dans le jeu
#           - Une paire de scores correspondant au score du joueur 1 et du score du joueur 2

game = None #Contient le module du jeu specifique: awele ou othello
joueur1 = None #Contient le module du joueur 1
joueur2 = None #Contient le module du joueur 2


#Fonctions minimales 

def getCopieJeu(jeu):
    """ jeu->jeu
        Retourne une copie du jeu passe en parametre
        Quand on copie un jeu on en calcule forcement les coups valides avant
    """
    jeu[2] = getCoupsValides(jeu)
    return deepcopy(jeu)
    

def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
    """
    return game.finJeu(jeu)
    

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
        On suppose que la fonction n'est appelee que si il y a au moins un coup valide possible
        et qu'elle retourne obligatoirement un coup valide
    """
    joueur = getJoueur(jeu)
    if joueur == 1:
        joueur = joueur1
    else:
        joueur = joueur2
    coup = joueur.saisieCoup(getCopieJeu(jeu))
    while not coupValide(jeu, coup):
        print("votre coup n'est pas valide, recommencer")
        coup = joueur.saisieCoup(getCopieJeu(jeu))
    return coup

def joueCoup(jeu, coup):
    """jeu*coup->void
        Joue un coup a l'aide de la fonction joueCoup defini dans le module game
        Hypothese:le coup est valide
        Met tous les champs de jeu a  jour (sauf coups valides qui est fixe a  None)
    """
    return game.joueCoup(jeu, coup)
    
def coupValide(jeu, coup):
    """ Verifie si un coup est valide.

    Args:
        jeu: contexte de jeu
        coup: coup a verifie

    Returns:
        True si le coup est valide, False sinon
    """
    coups_valides = getCoupsValides(jeu)
    coup_y, coup_x = coup
    for coup_valide in coups_valides:
        coup_valide_y, coup_valide_x = coup_valide
        if coup_x == coup_valide_x and coup_y == coup_valide_y:
            return True
    return False

def initialiseJeu():
    """ void -> jeu
        Initialise le jeu (nouveau plateau, liste des coups joues vide, liste des coups valides None et joueur = 1)
    """
    plateau = game.initPlateau()
    scores = game.initScores()
    return [plateau, 1, None, list(), scores]  

def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    score = getScores(jeu)
    if score[0] < score[1]:
        return 2
    elif score[1] < score[0]:
        return 1
    return 0

def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer
                    
    Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """
    plateau, joueur, coups_possibles, coups_faits, score = jeu
    header = '     |' + '|'.join([ '{:5d}'.format(index) for index in range(len(plateau[0]))]) + '|'
    underline = '-' * len(header)
    print(header)
    for y in range(len(plateau)):
        print(underline)
        prefix = '{:5d}|'.format(y)
        line = prefix + '|'.join([ '{:5d}'.format(plateau[y][x]) for x in range(len(plateau[y])) ]) + '|'
        print(line)
    print(underline)
    

# Fonctions utiles

def getPlateau(jeu):
    """ jeu  -> plateau
        Retourne le plateau du jeu passe en parametre
    """
    plateau, joueur, coups_possibles, coups_faits, score = jeu
    return plateau

def getCoupsJoues(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups joues dans le jeu passe en parametre
    """
    plateau, joueur, coups_possibles, coups_faits, score = jeu
    return coups_faits

def getCoupsValides(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups valides dans le jeu passe en parametre
        Si None, alors on met Ã  jour la liste des coups valides
    """
    jeu[2] = game.getCoupsValides(jeu) # maj coups valides
    return jeu[2]
        
        

def getScores(jeu):
    """ jeu  -> Pair[nat nat]
        Retourne les scores du jeu passe en parametre
    """
    plateau, joueur, coups_possibles, coups_faits, score = jeu
    return score

def getJoueur(jeu):
    """ jeu  -> nat
        Retourne le joueur a qui c'est le tour de jouer dans le jeu passe en parametre
    """
    plateau, joueur, coups_possibles, coups_faits, score = jeu
    return joueur



def changeJoueur(jeu):
    """ jeu  -> void
        Change le joueur a qui c'est le tour de jouer dans le jeu passe en parametre (1 ou 2)
    """
    plateau, joueur, coups_possibles, coups_faits, score = jeu
    jeu[1] = 2 if joueur == 1 else 1


def getScore(jeu,joueur):
    """ jeu*nat->int
        Retourne le score du joueur
        Hypothese: le joueur est 1 ou 2
    """
    plateau, joueur, coups_possibles, coups_faits, score = jeu
    if joueur == 1:
        return score[joueur - 1]
    elif joueur == 2:
        return score[joueur - 1]


def getCaseVal(jeu, ligne, colonne):
    """ jeu*nat*nat -> nat
        Retourne le contenu de la case ligne,colonne du jeu
        Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
    """
    plateau_jeu = jeu[0]
    return plateau_jeu[ligne][colonne]
    
def setCaseVal(jeu, ligne, colonne, value):
    """ Initialize une case du jeu.

    Args:
        jeu: contexte de jeu
        ligne: indice ligne
        colonne: indice colonne
        value: valeur a ajouter
    """
    plateau_jeu = jeu[0]
    plateau_jeu[ligne][colonne] = value
    
def addCaseVal(jeu, ligne, colonne, value):
    """ Ajoute une valeur a une case du jeu.

    Args:
        jeu: contexte de jeu
        ligne: indice ligne
        colonne: indice colonne
        value: valeur a ajouter
    """
    plateau_jeu = jeu[0]
    plateau_jeu[ligne][colonne] += value
    
def addCoupJoue(jeu, coup):
    """ Ajoute un coup fait.

    Args:
        jeu: contexte de jeu
        coup: coup a ajouter
    """
    coups_joues = jeu[3]
    coups_joues.append(coup)
    
def razCoupsValides(jeu):
    """ Reinitialise la liste de coups valides.

    Args:
        jeu: plateau de jeu
    """
    jeu[2] = list() # coups valides
    
def addScore(jeu, joueur, value):
    """ Mets a jour le score.

    Args:
        jeu: contexte de jeu
        joueur: numero du joueur
        value: valeur a ajouter au score du joueur
    """
    scores = getScores(jeu)
    scores[joueur - 1] += value 
