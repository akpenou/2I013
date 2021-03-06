import sys
sys.path.append("../..")
import game

inf=4
def evaluation (jeu,moi):
    adv=moi%2+1
    score = 0
    for x in range(8):
        for y in range(8):
            add = 1
            if (x == 0 and y == 1) or (x == 1 and 0 <= y <= 1):
                if jeu[0][0][0] == moi:
                    add = 5
                else:
                    add = -5

            elif (x == 0 and y == 6) or (x == 1 and 6 <= y <= 7):
                if jeu[0][7][0] == moi:
                    add = 5
                else:
                    add = -5
            elif (x == 7 and y == 1) or (x == 6 and 0 <= y <= 1):
                if jeu[0][0][7] == moi:
                    add = 5
                else:
                    add = -5

            elif (x == 7 and y == 6) or (x == 6 and 6 <= y <= 7):
                if jeu[0][7][7] == moi:
                    add = 5
                else:
                    add = -5

            if (x == 0 or y == 0 or x == 7 or y == 7):
                add = 5

            elif (x == 0 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 0) or (x == 7 and y == 7):
                add = 25

            if (jeu[0][x][y] == moi):
                score += add
            
            elif (jeu[0][x][y] == adv):
                score -= add

    return score

def saisieCoup(jeu):
    coup=decision(jeu,game.getCoupsValides(jeu))
    return coup

def estimation(jeu,coup,profondeur,alpha,beta):
#Estimation :retourne un score d’utilité estimée pour un coup donné à partir d’un état de jeu courant
    moi=game.getJoueur(jeu)
    copie=game.getCopieJeu(jeu)
    game.joueCoup(copie,coup)
    if game.finJeu(copie):
        g=game.getGagnant(copie)
        if g == moi :
        	return 10000
        else:
            if g == 0 :
                return -100
            else :
                return -10000
    if profondeur == inf :
        return evaluation(copie,moi)
    else :
        liste= game.getCoupsValides(copie)
        if(profondeur%2==0) :
            best=10000
        else:
            best=-10000
        for coup in liste:
            valeur = estimation(jeu,coup,profondeur+1,alpha,beta)
            if( profondeur%2 == 1):
                if (valeur < best):
                    best = valeur
                if best < beta:
                    beta = best
                if alpha >= best:
                        return best+1
            else:
                if (valeur > best):
                    best = valeur
                if best > alpha:
                    alpha = best
                if best >= beta:
                        return best-1
        return best
            			
            			
            			
def decision(jeu, coups):
    #retourne le meilleur  coup et son score
    alpha = -10000
    beta = 10000
    temp = -10000
    max_coup = coups[0]
    for coup in coups:
        valeur = estimation(jeu, coup, 1, alpha, beta)
        if valeur > alpha:
            alpha = valeur
            max_coup = coup
        alpha = temp
    return max_coup

