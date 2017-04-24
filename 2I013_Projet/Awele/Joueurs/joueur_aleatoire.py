import sys
sys.path.append("../..")
import game
from random import choice

def saisieCoup(jeu):
	Liste=game.getCoupsValides(jeu)
	return choice(Liste)
