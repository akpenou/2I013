import sys
sys.path.append("../..")
import game

PROFONDEUR = 2

def saisieCoup(jeu):
    joueur=game.getJoueur(jeu)
    alpha = -128
    beta = 128
    temp = -128
    coups=game.getCoupsValides(jeu)
    max_coup = coups[0]
    global nodes
    nodes = 0
    for coup in coups:
        valeur = estimation(game.getCopieJeu(jeu), joueur, coup, PROFONDEUR, alpha, beta)
        if valeur > temp:
            # print('update decision:', valeur, temp)
            temp = valeur
            max_coup = coup
            alpha=valeur
    res = nodes
    return (max_coup, res)
    
def evaluation(jeu, joueur):
    score=game.getScores(jeu)
    if joueur==1:
        return score[0]-score[1]
    else:
        return score[1]-score[0]
    
def estimation(jeu, joueur, coup, profondeur, alpha, beta):
    global nodes
    nodes += 1
    game.joueCoup(jeu, coup)
    if (profondeur <= 0) or game.finJeu(jeu):
        return evaluation(game.getCopieJeu(jeu), joueur)
    liste= game.getCoupsValides(jeu)
    if len(liste) != 0:
        if(joueur == game.getJoueur(jeu)):
            temp=alpha
            for i in liste:
                valeur = estimation(game.getCopieJeu(jeu),joueur,i,profondeur-1,temp,beta)
                if( valeur >= beta):
                    return valeur
                if ( temp < valeur ):
                    temp = valeur
        else:
            temp=beta
            for i in liste :
                valeur = estimation(game.getCopieJeu(jeu),joueur,i,profondeur-1,alpha, temp)
                if (valeur <= alpha):
                    return valeur 
                if valeur < temp :
                    temp = valeur 
        return temp
    else :
        if (joueur == game.getJoueur(jeu)):
        	return -20
        else:
        	return 20
