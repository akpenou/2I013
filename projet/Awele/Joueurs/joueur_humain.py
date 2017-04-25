import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    coup_x = int(input("Joueur{:d} : quelle colonne ?".format(game.getJoueur(jeu))))
    coup = [game.getJoueur(jeu) - 1, coup_x]
    while not game.coupValide(jeu,coup):
        coup_x = int(input("Coup non valide, recommencez"))
        coup = [game.getJoueur(jeu) - 1, coup_x]
    return coup
