import sys
sys.path.append("../..")
import game


def saisiecoup(jeu):
    coup=decision(jeu)
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
	game.joueCoups(copie,jeu)
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
		m=10000
		for i in liste:
			e = estimation(jeu,i,profondeur,alpha,beta)
			if( profondeur%2 == 0):
				if (m < e):
					m = e
        			if alpha < m:
            				alpha = m
        			if m >= beta:
            				return m +1
    				return m
    			else :
    				if(m > e):
            				m = e 
        			if beta > m:
            				beta = m
        			if m <= alpha:
            				return m -1 
            			return m
            			
            			
            			
def decision(jeu):
#Decision :retourne la paire [Coup . Score] dont le score correspond au score d’évaluation maximal de la liste de coups passée en paramètre
	alpha= -10000000000000
    	beta = 10000000000000
   
    	liste_coup = game.getCoupsValides(jeu)
    	L=[]
    	index=0
    	for i in range (len(liste_coup)):
        	k = estimation(game.getCopieJeu(jeu),liste_coup[i],4,alpha,beta)
        	if (moi == 1) :
            		if (k>=alpha):
                		index = i
                		alpha = k
        	else :
            		if (k>alpha):
                		index = i
                		alpha = k
    	return liste_coup[index]


