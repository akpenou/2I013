import sys
sys.path.append("../..")
import game
inf = 4

def saisieCoup(jeu):
    return alpha_beta(jeu, 1, -10000, 10000)[1]
    
def evaluation(jeu,joueur):
    return sum(jeu[0][joueur - 1]) - sum(jeu[0][joueur % 2])
    if joueur==1:
        return score[1] - score[0]
    else:
        return score[0] - score[1]

INFINITY = 10000
INF = 5

def alpha_beta(jeu, profondeur, alpha, beta):
    if game.finJeu(jeu):
        winner = game.getGagnant(jeu)
        if winner:
            return (10000 if winner == game.getJoueur(jeu) else -10000), [12, 15]
        return -100, [12, 15]
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
