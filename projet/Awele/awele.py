import sys
sys.path.append("..")
sys.path.append("../..")
import game



def initPlateau():
    """void->plateau
        initialise le plateau
    """
    #Plateau:list[list[int]]
    plateau = [ [ 4 for x in range(6) ] for y in range(2) ]
    return plateau
	
	
def initScores():
    """void->tuple[int,int]
    initialise score
    """
    return [0, 0]
	
def finJeu(jeu):
    score = game.getScores(jeu)
    #print ('awele - finjeu - liste coups valides:', game.getCoupsValides(jeu))
    return not len(game.getCoupsValides(jeu)) or score[0] >= 25 or score[1] >= 25
	
def getCoupsValides(jeu):
    is_affame = adversaireAffame(jeu)
    cases_pleines = coups(jeu) # retourne la liste des cases du joueur contenant au moins une graine       
    if not is_affame:
        return cases_pleines
    coups_valides = list()
    for coup in cases_pleines:
        x = coup[1]
        y = coup[0]
        value = game.getCaseVal(jeu, y, x)
        if not y:
            if value > x:
                coups_valides.append(coup)
        else :
            if value >= 6 - x:
                coups_valides.append(coup)
    return coups_valides


def joueCoups(jeu, coup):
    value = game.getCaseVal(jeu, coup[0], coup[1])
    game.setCaseVal(jeu, coup[0], coup[1], 0)
    distribue(jeu, coup, value)
    game.addCoupJoue(jeu, coup)
    game.changeJoueur(jeu)
    game.razCoupsValides(jeu)

	
def distribue(jeu, coup, nb):
    tmp_coup = coup
    graines = list()
    while (nb > 0) :            
        tmp_coup = nextCase(jeu, tmp_coup, True)
        if tmp_coup[0] == coup[0] and tmp_coup[1] == coup[1]:
            continue
        game.addCaseVal(jeu, tmp_coup[0], tmp_coup[1], 1)
        nb -= 1
    while peutManger(jeu, tmp_coup):
        value = game.getCaseVal(jeu, tmp_coup[0], tmp_coup[1])
        graines.append(value)
        game.setCaseVal(jeu, tmp_coup[0], tmp_coup[1], 0)
        game.addScore(jeu, game.getJoueur(jeu), value)
        tmp_coup = nextCase(jeu, tmp_coup, False)
    if len(graines) > 0 and adversaireAffame(jeu):
        index = 1
        while index <= len(graines):
            tmp_coup = nextCase(jeu, tmp_coup, True)
            tmp_graine = graines[-index]
            game.setCaseVal(jeu, tmp_coup[0], tmp_coup[1], tmp_graine)
            game.addScore(jeu, game.getJoueur(jeu), -tmp_graine)  
            index += 1


def peutManger(jeu, coup):
    """jeu * Pair[nat nat] -> bool
        Retourne vrai si on peut manger le contenu de la case:
            - c'est une case appartenant a l'adversaire du joueur courant
            - La case contient 2 ou 3 graines
    """
    coup_y, coup_x = coup
    if coup_y == game.getJoueur(jeu) - 1:
        return False
    value = game.getCaseVal(jeu, coup_y, coup_x)
    if value not in [2, 3]:
        return False
    return True
	

def adversaireAffame(jeu):
     joueur = game.getJoueur(jeu)
     joueur = joueur % 2 + 1 #on recupere le joueur adverse
     for index in range(6):
          coup = game.getCaseVal(jeu, joueur - 1, index)
          if coup:
               return False
     return True


def nextCase(jeu, coup, antihoraire = True):
    sens = 1
    coup_y, coup_x = coup
    if antihoraire:
        # if coup_y != 1:
        #     return [coup_y, case]        
        if coup_y == 1:
            case = coup_x + sens #dans le cas ou on se trouve sur la 2eme ligne
        if not coup_y:
            case = coup_x - sens #dans le cas ou on se trouve sur la 1ere ligne
        if case < 0 and not coup_y: #dans le cas ou on se trouve dans la 1ere ligne 1ere colonne dans le sens -1
            return [1, 0]
        if case > 5 and coup_y == 1 :
            return [0, 5]
        return [coup_y, case]
    else:
        if coup_y == 1:
            case = coup_x - sens #dans le cas ou on se trouve sur la 2eme ligne
        if not coup_y:
            case = coup_x + sens #dans le cas ou on se trouve sur la 1ere ligne 
        if case < 0 and coup_y == 1:
            return [0, 0]
        if case > 5 and not coup_y:
            return [1, 5]
        return [coup[0], case]


def coups(jeu):
     graines = list()
     joueur = game.getJoueur(jeu)
     for index in range(6):
          value = game.getCaseVal(jeu, joueur - 1 , index)
          if value:
               graines.append([joueur - 1, index])
     return graines
	

def finalisePartie(jeu):
    """jeu->void
        Met a jour les scores des joueurs en prenant en compte les graines restantes sur le plateau
    """
    plateau_jeu = game.getPlateau(jeu)
    graines_1 = sum(plateau_jeu[0])
    graines_2 = sum(plateau_jeu[1])
    game.addScore(jeu, 1, graines_1)
    game.addScore(jeu, 2, graines_2)
