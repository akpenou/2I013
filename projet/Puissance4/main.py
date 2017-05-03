import puissance4
import time
import sys
sys.path.append("..")
import game
game.game=puissance4
sys.path.append("./Joueurs")
import joueur_humain
# import premier_coup_valide
import joueur_aleatoire
# import alphabeta_player
import alphabeta_player_winner
import alphabeta_player_winner_2
import alphabeta_player_winner_3
from random import choice
# import alphabeta_v
# import deep_5
# import deep_4
# import deep_3
# import deep_2

class Stats():
    def __init__(self, player, name):
        self.player = player
        self.name = name
        self.times = list()
        self.wins = 0
        self.nodes = list()

    def add_time(self, _time):
        self.times.append(_time)

    def add_win(self):
        self.wins += 1

    def add_node(self, node):
        self.nodes.append(node)

    def get_result(self, _file = None):
        times = sum(self.times) / len(self.times)
        nodes = sum(self.nodes) / len(self.nodes) if self.nodes else 0
        print('nodes:', nodes)
        if _file:
            print(self.player, ',', self.name, ',', times, ',', self.wins, ',', nodes, file = _file)
        else:
            print(self.player, ',', self.name, ',', times, ',', self.wins, ',', nodes)

#game.joueur1=joueur_aleatoire
# if sys.argv[1] == '1':
#     player1 = Stats(1, 'premier_coup_valide')
#     game.joueur1 = premier_coup_valide
#     player2 = Stats(2, 'premier_coup_valide')
#     game.joueur2 = premier_coup_valide
# elif sys.argv[1] == '2':
#     player1 = Stats(1, 'joueur_aleatoire')
#     game.joueur1 = joueur_aleatoire
#     player2 = Stats(2, 'premier_coup_valide')
#     game.joueur2 = premier_coup_valide
# elif sys.argv[1] == '3':
#     player1 = Stats(1, 'alphabeta_v')
#     game.joueur1 = alphabeta_v
#     player2 = Stats(2, 'premier_coup_valide')
#     game.joueur2 = premier_coup_valide
# elif sys.argv[1] == '4':
#     player1 = Stats(1, 'premier_coup_valide')
#     game.joueur1 = premier_coup_valide
#     player2 = Stats(2, 'joueur_aleatoire')
#     game.joueur2 = joueur_aleatoire
# elif sys.argv[1] == '5':
#     player1 = Stats(1, 'joueur_aleatoire')
#     game.joueur1 = joueur_aleatoire
#     player2 = Stats(2, 'joueur_aleatoire')
#     game.joueur2 = joueur_aleatoire
# elif sys.argv[1] == '6':
#     player1 = Stats(1, 'alphabeta_v')
#     game.joueur1 = alphabeta_v
#     player2 = Stats(2, 'joueur_aleatoire')
#     game.joueur2 = joueur_aleatoire
# elif sys.argv[1] == '7':
#     player1 = Stats(1, 'premier_coup_valide')
#     game.joueur1 = premier_coup_valide
#     player2 = Stats(2, 'alphabeta_v')
#     game.joueur2 = alphabeta_v
# elif sys.argv[1] == '8':
#     player1 = Stats(1, 'joueur_aleatoire')
#     game.joueur1 = joueur_aleatoire
#     player2 = Stats(2, 'alphabeta_v')
#     game.joueur2 = alphabeta_v
# elif sys.argv[1] == '9':
#     player1 = Stats(1, 'alphabeta_v')
#     game.joueur1 = alphabeta_v
#     player2 = Stats(2, 'alphabeta_v')
#     game.joueur2 = alphabeta_v
# else:
#     print('deep')
#     player1 = Stats(1, 'deep_3')
#     game.joueur1 = deep_3
#     player2 = Stats(2, 'deep_2')
#     game.joueur2 = deep_2

player1 = Stats(1, 'joueur_aleatoire')
player2 = Stats(2, 'alphabeta_player_winner_3')
game.joueur1 = joueur_aleatoire
game.joueur2 = alphabeta_player_winner_3

resultat = [0, 0]
for index in range(10):
    jeu = game.initialiseJeu()
    print("Partie n {:d}".format(index))
    index = 0
    for index in range(4):
        coups = game.getCoupsValides(jeu)
        game.joueCoup(jeu, choice(coups))
    game.affiche(jeu)
    print('---')
    while not game.finJeu(jeu):
        # game.affiche(jeu)
        # print('---', game.getJoueur(jeu))
        # if not index % 20:
        index += 1
        # Block avec joueurs
        current = time.time()
        coup = game.saisieCoup(jeu)
        # coup, nodes = res
        current = time.time() - current
        # print(coup, '|', nodes, flush = True)
        if index % 2:
            player1.add_time(current)
        #     player1.add_node(_nodes)
        else:
            player2.add_time(current)
        #     player2.add_node(_nodes)
        # End block avec joueurs
        game.joueCoup(jeu, coup)
    gagnant = game.getGagnant(jeu)
    if gagnant == 1:
        resultat[0] += 1
        player1.add_win()
    elif gagnant == 2:
        resultat[1] += 1
        player2.add_win()
    game.affiche(jeu)
    player1.get_result()
    player2.get_result()
    print('res:', resultat, game.getScores(jeu))

with open('res.csv', 'a') as f:
    player1.get_result(f)
    player2.get_result(f)
   
print("Joueur 1 a gagne {:d}, Joueur 2 a gagne {:d}".format(resultat[0], resultat[1]))
