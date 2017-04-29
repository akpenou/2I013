import sys
sys.path.append("../..")
import game
inf = 4

def saisieCoup(jeu):
    # coup=decision(jeu,game.getCoupsValides(jeu))
    return alpha_beta(jeu, 1, -10000, 10000)[1]

    

    
def evaluation(jeu,joueur):
    score=game.getScores(jeu)
    if joueur==1:
        return score[1]-score[0]
    else:
        return score[0]-score[1]


def estimation(jeu,coup,profondeur,alpha,beta):
#Estimation :retourne un score d utilite estimee pour un coup donne a partir d un etat de jeu courant
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
        for i in liste:
            valeur = estimation(jeu,i,profondeur+1,alpha,beta)
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
            			
            			
INFINITY = 10000
INF = 4

def decision(jeu, coups):
    #retourne le meilleur  coup et son score
    alpha = -10000
    beta = 10000
    temp = -10000
    max_coup = coups[0]
    for coup in coups:
        valeur = estimation(jeu, coup, 1, alpha, beta)
        if valeur > temp:
            temp = valeur
            max_coup = coup
    return max_coup

def alpha_beta(jeu, profondeur, alpha, beta):
    if game.finJeu(jeu):
        winner = game.getGagnant(jeu)
        if winner:
            return (10000 if winner == game.getJoueur(jeu) else -10000), [12, 15]
        return -100, [12, 15]
    if profondeur == INF:
        return evaluation(jeu, game.getJoueur(jeu)), None
    value = INFINITY * (1 if not profondeur % 2 else -1)
    jeu = game.getCopieJeu(jeu)
    for index, coup in enumerate(game.getCoupsValides(jeu)):
        game.joueCoup(jeu, coup)
        if not profondeur % 2:
            value = min([value, alpha_beta(jeu, profondeur + 1, alpha, beta)[0]])
            if alpha >= value:
                return value, coup
            beta = min(beta, value)
        else:
            value = max([value, alpha_beta(jeu, profondeur + 1, alpha, beta)[0]])
            if value >= beta:
                return value, coup
            beta = max(beta, value)
    return value, coup
