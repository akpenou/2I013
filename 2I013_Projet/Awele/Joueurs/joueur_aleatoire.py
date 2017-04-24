import sys
sys.path.append("../..")
import game
from random import choice

def saisieCoup(jeu):
	coups_valides = game.getCoupsValides(jeu)
	return choice(coups_valides)
