import sys
sys.path.append("../..")
import game

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

    
def evaluation(jeu,joueur):
    return (corner_capture(jeu, joueur) + stability(jeu, joueur) + coin_parity(jeu, joueur)) / 3

def saisieCoup(jeu):
    joueur=game.getJoueur(jeu)
    alpha = -128
    beta = 128
    temp = -128
    coups=game.getCoupsValides(jeu)
    max_coup = coups[0]
    global nodes
    nodes = 0
    for coup in coups:
        valeur = estimation(game.getCopieJeu(jeu), joueur, coup, 3, alpha, beta)
        if valeur > temp:
            # print('update decision:', valeur, temp)
            temp = valeur
            max_coup = coup
            alpha=valeur
    return max_coup, nodes
    
    
def estimation(jeu, joueur, coup, profondeur, alpha, beta):
    global nodes
    nodes += 1
    game.joueCoup(jeu, coup)
    if (profondeur <= 0) or game.finJeu(jeu):
        return evaluation(game.getCopieJeu(jeu), joueur)
    liste= game.getCoupsValides(jeu)
    if len(liste) != 0:
        if(joueur == game.getJoueur(jeu)):
            temp=alpha
            for i in liste:
                valeur = estimation(game.getCopieJeu(jeu),joueur,i,profondeur-1,temp,beta)
                if( valeur >= beta):
                    return valeur
                if ( temp < valeur ):
                    temp = valeur
        else:
            temp=beta
            for i in liste :
                valeur = estimation(game.getCopieJeu(jeu),joueur,i,profondeur-1,alpha, temp)
                if (valeur <= alpha):
                    return valeur 
                if valeur < temp :
                    temp = valeur 
        return temp
    else :
        if (joueur == game.getJoueur(jeu)):
        	return -20
        else:
        	return 20

def stats(jeu, joueur, score):
    if not hasattr(stats, 'meta'):
        try:
            with open('stats.json') as f:
                stats.meta = json.load(f)
        except Exception as e:
            print('can\'t find the file:', e)
            stats.meta = { 'array': [ [ 0 for x in range(8) ] for y in range(8) ], 'index': 0 }
    array = stats.meta['array']
    stats.meta['index'] += 1
    for x in range(8):
        for y in range(8):
            if jeu[0][y][x] == joueur:
                array[0][y][x] += score
            elif jeu[0][y][x]:
                array[0][y][x] -= score
    with open('stats.json', 'w') as f:
        json.dump(stats.meta, f)
