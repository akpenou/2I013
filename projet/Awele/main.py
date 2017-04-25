import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
import joueur_aleatoire
import joueur_alphabeta
game.joueur2=joueur_aleatoire
game.joueur1=joueur_aleatoire

resultat = [0, 0]
for index in range(1000):
    jeu = game.initialiseJeu()
    print("Partie n°{:d}".format(index))
    while not game.finJeu(jeu):
        game.getCoupsValides(jeu)
        coup = game.saisieCoup(jeu)
        game.joueCoups(jeu, coup)
    gagnant = game.getGagnant(jeu)
    if gagnant == 1:
        resultat[0] += 1
    elif gagnant == 2:
        resultat[1] += 1
#game.affiche(jeu)
    print("Le gagnant est : {:d}".format(gagnant))
    break
print("Joueur 1 a gagne {:d}, Joueur 2 a gagne {:d}".format(resultat[0], resultat[1]))
