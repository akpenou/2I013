import sys
sys.path.append("../..")
import game


def saisieCoup(jeu):
    joueur=game.getJoueur(jeu)
    alpha = -128
    beta = 128
    temp = -128
    coups=game.getCoupsValides(jeu)
    max_coup = coups[0]
    for coup in coups:
        valeur = estimation(game.getCopieJeu(jeu), joueur, coup, 5, alpha, beta)
        if valeur > temp:
            #print('score:', valeur, coup)
            # #print('update decision:', valeur, temp)
            temp = valeur
            max_coup = coup
            alpha=valeur
    return max_coup
    
def evaluation(jeu, joueur):
    score=game.getScores(jeu)
    if joueur==1:
        return score[0]-score[1]
    else:
        return score[1]-score[0]
    
def estimation(jeu, joueur, coup, profondeur, alpha, beta):
    game.joueCoup(jeu, coup)
    #print('play:', coup, profondeur, alpha, beta)
    if (profondeur <= 0) or game.finJeu(jeu):
        res = evaluation(game.getCopieJeu(jeu), joueur)
        #print('res:', res, coup, alpha, beta)
        return res
    liste= game.getCoupsValides(jeu)
    if len(liste) != 0:
        if(joueur == game.getJoueur(jeu)):
            temp=alpha
            for i in liste:
                valeur = estimation(game.getCopieJeu(jeu),joueur,i,profondeur-1,temp,beta)
                if( valeur >= beta):
                    #print('prune:', valeur, coup, valeur, beta)
                    return valeur
                if ( temp < valeur ):
                    temp = valeur
        else:
            temp=beta
            for i in liste :
                valeur = estimation(game.getCopieJeu(jeu),joueur,i,profondeur-1,alpha, temp)
                if (valeur <= alpha):
                    #print('prune:', valeur, coup, alpha, valeur)
                    return valeur 
                if valeur < temp :
                    temp = valeur 
        #print('test:', temp, coup)
        return temp
    else :
        if (joueur == game.getJoueur(jeu)):
        	return -20
        else:
        	return 20
