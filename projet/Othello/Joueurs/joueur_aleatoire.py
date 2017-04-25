import sys
sys.path.append("../..")
import game
from random import choice


def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    Liste=game.getCoupsValides(jeu) 
    return choice(Liste)
    
   
