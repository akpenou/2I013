import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_humain
import joueur_minmax
import premier_coup_valide
import joueur_aleatoire
import joueur_alphabeta
game.joueur1=joueur_aleatoire
game.joueur2=joueur_alphabeta

resultat = [0, 0]
for index in range(10):
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
  
   
print("Joueur 1 a gagne {:d}, Joueur 2 a gagne {:d}".format(resultat[0], resultat[1]))
