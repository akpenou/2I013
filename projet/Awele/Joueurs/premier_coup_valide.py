import sys
sys.path.append("../..")
import game



def saisieCoup(jeu):
    Liste=game.getCoupsValides(jeu)
    coup = Liste[0]
    return coup
