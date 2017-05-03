import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    coup = int(input("Joueur{:d} : quelle colonne ?".format(game.getJoueur(jeu))))
    while not game.coupValide(jeu,coup):
        coup = int(input("Coup non valide, recommencez"))
    return coup
