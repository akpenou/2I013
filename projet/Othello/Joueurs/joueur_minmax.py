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
p=4

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
	if profondeur >= p :
		return evaluation(copie)
	else :
		liste= game.getCoupsValides(copie)
		m=10000
		for i in liste:
			e = estimation(jeu,i,profondeur)
			if( profondeur%2 == 0):
				if (m < e):
					m = e
    				return m
    			else :
    				if(m > e):
            				m = e 
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
