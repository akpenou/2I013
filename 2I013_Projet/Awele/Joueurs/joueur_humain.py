import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
	c=input("Joueur"+str(game.getJoueur(jeu))+" : quelle colonne ? ")
	coup=[game.getJoueur(jeu)-1,c]
	while(not(game.coupValide(jeu,coup))):
		c=input("Coup non valide, recommencez")
		coup=[game.getJoueur(jeu)-1,c]
	return coup
