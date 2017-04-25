import sys
sys.path.append("../..")
import game



def saisieCoup(jeu):
	L=game.getCoupsValides(jeu)
 	c=L[0]
	return c
