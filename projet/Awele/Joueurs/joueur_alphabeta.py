import sys
sys.path.append("../..")
import game
inf=4

def saisieCoup(jeu):
    coup=decision(jeu,game.getCoupsValides(jeu))
    return coup

      
def eval_score(jeu,moi):
    """retourne le score de moi"""
    L = game.getScores(jeu)
    x = moi - 1
    return L[x]   
    
 
def eval_graineJ(jeu,moi): 
    """ Evalue le nombre de cases du joueur avec 1 ou 2 graines """   
    for i in range (0, 5):
        graine = game.getCaseVal(jeu,moi-1,i)
        if (graine == 1) or (graine == 2):
            graine+=1
    return graine

        
def eval_graineA(jeu,moi): 
    """ Evalue le nombre de cases de l adversaire avec 1 ou 2 graines """    
    adv = moi % 2 
    for i in range (0, 5):
        graine = game.getCaseVal(jeu,adv,i)
        if (graine == 1) or (graine == 2):
            graine+=1
    return graine
    
def evaluation(jeu,joueur):
    a = 0.5
    b = -1
    c = 1 
    return a * eval_score(jeu,joueur) + b * eval_graineJ(jeu,joueur) + c * eval_graineA(jeu,joueur)


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


