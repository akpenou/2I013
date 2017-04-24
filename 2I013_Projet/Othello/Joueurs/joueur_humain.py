import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
	"""Jeu -> coup"""
	print("Joueur"+str(game.getJoueur(jeu)))
	c=input("Quelle colonne ? ")
	l=input("Quelle ligne ? ")
	coup=[l,c]
	while(not(game.coupValide(jeu,coup))):
		print("Coup non valide, recommencez")
		c=input("Quelle colonne ? ")
		l=input("Quelle ligne ? ")
		coup=[l,c]
	return coup
 
