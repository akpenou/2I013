import sys
sys.path.append("../..")
import game
inf = 4

def coin_parity(jeu, joueur):
    max_player_coins = sum([ 1 for line in jeu[0] 
                            for case in line
                            if case == joueur ])
    min_player_coins = sum([ 1 for line in jeu[0] 
                            for case in line
                            if case == (joueur + 1) % 2])
    return 100 * (max_player_coins - min_player_coins) / (max_player_coins + min_player_coins)


def stability(jeu, joueur):
    stability_coef = [[  4, -3,  2,  2,  2,  2, -3,  4],
                      [ -3, -4, -1, -1, -1, -1, -4, -3],
                      [  2, -1,  1,  0,  0,  1, -1,  2],
                      [  2, -1,  0,  1,  1,  0, -1,  2],
                      [  2, -1,  0,  1,  1,  0, -1,  2],
                      [  2, -1,  1,  0,  0,  1, -1,  2],
                      [ -3, -4, -1, -1, -1, -1, -4, -3],
                      [  4, -3,  2,  2,  2,  2, -3,  4]]
    max_player_stability = sum([ stability_coef[y][x] for y in range(8)
                                                  for x in range(8)
                                                  if jeu[0][y][x] == joueur ])
    min_player_stability = sum([ stability_coef[y][x] for y in range(8)
                                                  for x in range(8)
                                                  if jeu[0][y][x] == (joueur + 1) % 2 + 1 ])
    if max_player_stability + min_player_stability:
        return 100 * (max_player_stability - min_player_stability) / (max_player_stability + min_player_stability)
    return 0

def mobility_test(jeu, joueur, coord):
    res = 0
    x, y = coord
    if x > 0 and not jeu[0][y][x - 1]:
        res += 1
    if x < 7 and not jeu[0][y][x + 1]:
        res += 1
    if y > 0 and not jeu[0][y - 1][x]:
        res += 1
    if y < 7 and not jeu[0][y + 1][x]:
        res += 1
    return res


def potential_mobility(jeu, joueur):
    max_potential_mobility = sum([ mobility_test(jeu, joueur, (x, y))
                                for y in range(8)
                                for x in range(8) ])
    min_potential_mobility = sum([ mobility_test(jeu, (joueur + 1) % 2 + 1, (x, y))
                                for y in range(8)
                                for x in range(8) ])
    if max_potential_mobility + min_potential_mobility:
        return 100 * (max_potential_mobility - min_potential_mobility) / (max_potential_mobility + min_potential_mobility)
    return 0


def actual_mobility(jeu, joueur):
    max_actual_mobility = len(game.getCoupsValides(jeu))
    jeu[1] = (joueur + 1) % 2 + 1
    min_actual_mobility = len(game.getCoupsValides(jeu))
    jeu[1] = joueur
    if max_actual_mobility + min_actual_mobility:
        return 100 * (max_actual_mobility - min_actual_mobility) / (max_actual_mobility + min_actual_mobility)
    return 0


def corner_capture(jeu, joueur):
    max_corner_capture = sum([ 1 for x, y in [(0, 0), (7, 0), (7, 7), (0, 7)] if jeu[0][y][x] == joueur ])
    min_corner_capture = sum([ 1 for x, y in [(0, 0), (7, 0), (7, 7), (0, 7)] if jeu[0][y][x] == (joueur + 1) % 2 + 1 ])
    if max_corner_capture + min_corner_capture:
        return 100 * (max_corner_capture - min_corner_capture) / (max_corner_capture + min_corner_capture)
    return 0


def saisieCoup(jeu):
    return alpha_beta(jeu, 1, -1000, 1000)[1]
    
def evaluation(jeu,joueur):
    return (corner_capture(jeu, joueur) + actual_mobility(jeu, joueur) + potential_mobility(jeu, joueur) + stability(jeu, joueur) + coin_parity(jeu, joueur)) / 5

INFINITY = 100
INF = 4

def alpha_beta(jeu, profondeur, alpha, beta):
    if game.finJeu(jeu):
        winner = game.getGagnant(jeu)
        if winner:
            return (1000 if winner == game.getJoueur(jeu) else -1000), None
        return -100, None
    if profondeur == INF:
        return evaluation(jeu, game.getJoueur(jeu)), None
    value = INFINITY * (1 if not profondeur % 2 else -1)
    jeu = game.getCopieJeu(jeu)
    for index, coup in enumerate(game.getCoupsValides(jeu)):
        game.joueCoup(jeu, coup)
        if not profondeur % 2:
            value = min([value, alpha_beta(jeu, profondeur + 1, alpha, beta)[0]])
            if alpha >= value:
                return value, coup
            beta = min(beta, value)
        else:
            value = max([value, alpha_beta(jeu, profondeur + 1, alpha, beta)[0]])
            if value >= beta:
                return value, coup
            beta = max(beta, value)
    return value, coup
