import sys
sys.path.append("../..")
import game
inf=4

def saisieCoup(jeu):
    coup=decision(jeu,game.getCoupsValides(jeu))
    return coup


def evaluation(jeu):
#Evaluation :retourne un score d’évaluation d’un état de jeu
    moi=game.getJoueur(jeu)
    score =game.getScores(jeu)
    if moi == 1:
        return score[0] - score[1]
    else:
        return score[1] - score[0]  

def estimation(jeu,coup,profondeur,alpha,beta):
#Estimation :retourne un score d’utilité estimée pour un coup donné à partir d’un état de jeu courant
    moi=game.getJoueur(jeu)
    copie=game.getCopieJeu(jeu)
    game.joueCoups(copie,coup)
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
        return evaluation(copie)
    else :
        liste= game.getCoupsValides(copie)
        if(profondeur%2==0) :
            best=100000
        else:
            best=-100000
    for i in liste:
        valeur = estimation(jeu,i,profondeur+1,alpha,beta)
        if( profondeur%2 == 0):
            if (valeur < best):
                best = valeur
                if best < beta:
                    beta = best
                    if alpha > beta:
                        return best
        else:	
            if (valeur > best):
                best = valeur
                if best > alpha:
                    alpha = best
                    if alpha > best:
                        return best
    return best
            			
            			
            			
def decision(jeu, coups):
    #retourne le meilleur  coup et son score
    alpha = -100000
    beta = 100000
    alpha = estimation(jeu, coups[0], 1, alpha, beta)
    max_coup = coups[0]

    for c in coups:
        s = estimation(jeu, c, 1, alpha, beta)
        if s >= beta:
            break
        if s > alpha:
            alpha = s
            max_coup = c
    return max_coup


