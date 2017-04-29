"""l consiste donc à anticiper la réplique de l'adversaire
à un coup joué, puis la réplique de cette réplique ... ainsi de suite
jusqu'à une certaine condition d'arrêt. Une fois cette condition vérifiée,
l'algorithme utilisera une fonction d'évaluation qui permettra de rendre
compte de la situation dans laquelle se trouve un joueur étant donné
l'othellier. Min-max permet de retourner l'évaluation correspondant au
meilleur compromis maximisation-minimisation pouvant être fait à partir
d'une situation. Soit la meilleur évaluation en supposant que l'adversaire
ai une évaluation équivalente du jeu. """




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
	
    if profondeur >= inf :
        return evaluation(copie)
    else :
        liste= game.getCoupsValides(copie)
        best=10000
        for coup in liste:
            valeur = estimation(jeu,coup,profondeur+1,alpha,beta)
            if( profondeur%2 == 0):
                if (best < valeur):
                    best = valeur
                return best
            else :
                if(best > valeur):
                    best = valeur 
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

