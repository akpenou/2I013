import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
import premier_coup_valide
import joueur_aleatoire
import alphabeta_player
import alphabeta_player_winner
#game.joueur1=joueur_aleatoire
game.joueur1 = premier_coup_valide
game.joueur2 = alphabeta_player_winner

resultat = [0, 0]
for index in range(100):
    jeu = game.initialiseJeu()
    print("Partie n°{:d}".format(index))
    index = 0
    while not game.finJeu(jeu):
        if not index % 20:
            print('index:', index)
        index += 1
        game.getCoupsValides(jeu)
        coup = game.saisieCoup(jeu)
        game.joueCoup(jeu, coup)
    gagnant = game.getGagnant(jeu)
    if gagnant == 1:
        resultat[0] += 1
    elif gagnant == 2:
        resultat[1] += 1
    game.affiche(jeu)
    print('res:', resultat)
  
   
print("Joueur 1 a gagne {:d}, Joueur 2 a gagne {:d}".format(resultat[0], resultat[1]))
