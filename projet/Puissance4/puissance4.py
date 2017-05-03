import sys
sys.path.append("..")
sys.path.append("../..")
import game



def initPlateau():
    """void->plateau
        initialise le plateau
    """
    #Plateau:list[list[int]]
    plateau = [ [ 0 for x in range(7) ] for y in range(6) ]
    return plateau
	
	
def initScores():
    """void->tuple[int,int]
    initialise score
    """
    return [0, 0]

def find_alignment(jeu, position):
    x, y = position
    plateau = jeu[0]
    joueur = game.getCaseVal(jeu, y, x)
    res = [0, 0, 0, 0]
    if not joueur:
        return res
    res = [1, 1, 1, 1]
    tmp_x, tmp_y = position
    while 0 < tmp_x and tmp_y < 6 - 1:
        tmp_x -= 1
        tmp_y += 1
        if game.getCaseVal(jeu, tmp_y, tmp_x) == joueur:
            res[0] += 1
        else:
            break ;
    tmp_x, tmp_y = position
    while tmp_y < 6 - 1:
        tmp_y += 1
        if game.getCaseVal(jeu, tmp_y, tmp_x) == joueur:
            res[1] += 1
        else:
            break ;
    tmp_x, tmp_y = position
    while tmp_x < 7 - 1 and tmp_y < 6 - 1:
        tmp_x += 1
        tmp_y += 1
        if game.getCaseVal(jeu, tmp_y, tmp_x) == joueur:
            res[2] += 1
        else:
            break ;
    tmp_x, tmp_y = position
    while tmp_x < 7 - 1:
        tmp_x += 1
        if game.getCaseVal(jeu, tmp_y, tmp_x) == joueur:
            res[3] += 1
        else:
            break ;
    return res


def finJeu(jeu):
    score = game.getScores(jeu)
    for x, y in [ (x, y) for x in range(7) for y in range(6) ]:
        dleft, middle, dright, right = find_alignment(jeu, (x, y))
        #print('test jeu:', left, middle, right)
        if dleft >= 4 or middle >= 4 or dright >= 4 or right >= 4:
            game.addScore(jeu, game.getCaseVal(jeu, y, x), 1)
            return True
    return not game.getCoupsValides(jeu)


def getCoupsValides(jeu):
    plateau = jeu[0]
    rows = [ index for index, case in enumerate(plateau[5]) if case == 0 ]
    return rows


def joueCoup(jeu, coup):
    plateau = jeu[0]
    joueur = game.getJoueur(jeu)
    for index, line in enumerate(plateau):
        if line[coup] == 0:
            game.setCaseVal(jeu, index, coup, joueur)
            break
    game.addCoupJoue(jeu, coup)
    game.changeJoueur(jeu)
    game.razCoupsValides(jeu)
