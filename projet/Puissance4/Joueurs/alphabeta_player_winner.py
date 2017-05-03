import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    best_score = -1000
    for index, coup in enumerate(game.getCoupsValides(jeu)):
        jeu_copie = game.getCopieJeu(jeu)
        game.joueCoup(jeu_copie, coup)
        score = alpha_beta(jeu_copie, 5, -128, 128, 1, coup)
        if score > best_score:
            best_score = score
            best_coup = coup
    return best_coup

def find_alignment(jeu, position):
    x, y = position
    plateau = jeu[0]
    joueur = game.getCaseVal(jeu, y, x)
    res = [0, 0, 0, 0]
    if not joueur:
        return res
    res = [1, 1, 1, 1]
    tmp_x, tmp_y = position
    while 0 < tmp_x and tmp_y < 6 - 1:
        tmp_x -= 1
        tmp_y += 1
        if game.getCaseVal(jeu, tmp_y, tmp_x) == joueur:
            res[0] += 1
        else:
            break ;
    tmp_x, tmp_y = position
    while tmp_y < 6 - 1:
        tmp_y += 1
        if game.getCaseVal(jeu, tmp_y, tmp_x) == joueur:
            res[1] += 1
        else:
            break ;
    tmp_x, tmp_y = position
    while tmp_x < 7 - 1 and tmp_y < 6 - 1:
        tmp_x += 1
        tmp_y += 1
        if game.getCaseVal(jeu, tmp_y, tmp_x) == joueur:
            res[2] += 1
        else:
            break ;
    tmp_x, tmp_y = position
    while tmp_x < 7 - 1:
        tmp_x += 1
        if game.getCaseVal(jeu, tmp_y, tmp_x) == joueur:
            res[3] += 1
        else:
            break ;
    return res


def evaluation(jeu):
    if game.finJeu(jeu):
        return 20 if game.getGagnant(jeu) else 0
    joueur = game.getJoueur(jeu)
    score = game.getScores(jeu)
    value = 0
    for x, y in [ (x, y) for x in range(7) for y in range(6) ]:
        value += sum(find_alignment(jeu, (x, y)))
    return value


def alpha_beta(jeu, profondeur, alpha, beta, color, best_coup):
    if game.finJeu(jeu) or not profondeur:
        res = evaluation(jeu)
        return res * color
    best_value = -128
    for index, coup in enumerate(game.getCoupsValides(jeu)):
        jeu_copie = game.getCopieJeu(jeu)
        game.joueCoup(jeu_copie, coup)
        score = -alpha_beta(jeu_copie, profondeur - 1, -beta, -alpha, -color, coup)
        if score > best_value:
            best_value = score
            best_play = coup
        if score >= alpha:
            alpha = score
        if alpha >= beta:
            return alpha
    return 0
