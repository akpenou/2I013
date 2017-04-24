import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
import joueur_aleatoire
import joueur_alphabeta
game.joueur1=joueur_humain
game.joueur2=joueur_alphabeta

resultat = [0, 0]
for i in range(1000):
    jeu = game.initialiseJeu()
    print "Partie n°%d" % i
    while not game.finJeu(jeu):
        game.getCoupsValides(jeu)
        coup = game.saisieCoup(jeu)
        game.joueCoup(jeu, coup)

    g = game.getGagnant(jeu)
    if g == 1:
        resultat[0] += 1
    elif g == 2:
        resultat[1] += 1
#game.affiche(jeu)

    print "Le gagant est : %d" %  g

print "Joueur 1 a gagne %d, Joueur 2 a gagne %d" % (resultat[0], resultat[1])
