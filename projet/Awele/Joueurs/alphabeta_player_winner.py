import sys
sys.path.append("../..")
import game
inf = 4

def saisieCoup(jeu):
    best_score = -1000
    for index, coup in enumerate(game.getCoupsValides(jeu)):
        jeu_copie = game.getCopieJeu(jeu)
        game.joueCoup(jeu_copie, coup)
        #print('play:', coup, 5, -128, 128)
        score = alpha_beta(jeu_copie, 5, -128, 128, 1, coup)
        if score > best_score:
            #print('score:', score, coup)
            best_score = score
            best_coup = coup
    return best_coup

    
def evaluation(jeu):
    if game.finJeu(jeu):
        return 20 if game.getGagnant(jeu) else 0
    joueur = game.getJoueur(jeu)
    score = game.getScores(jeu)
    delta_score = score[0] - score[1] if joueur == 1 else score[1] - score[0]
    return delta_score # + running_game) / 2


def alpha_beta(jeu, profondeur, alpha, beta, color, best_coup):
    if game.finJeu(jeu) or not profondeur:
        res = evaluation(jeu)
        #print('res:', res, best_coup, alpha, beta)
        return res * color
    best_value = -128
    for index, coup in enumerate(game.getCoupsValides(jeu)):
        jeu_copie = game.getCopieJeu(jeu)
        game.joueCoup(jeu_copie, coup)
        #print('play:', coup, profondeur - 1, -beta, -alpha)
        score = -alpha_beta(jeu_copie, profondeur - 1, -beta, -alpha, -color, coup)
        if score > best_value:
            best_value = score
            best_play = coup
        if score >= alpha:
            alpha = score
        if alpha >= beta:
            #print('prune:', best_value, best_coup, alpha, beta)
            return alpha
    #if #printable:
    #    #print('fin score:', alpha)
    #print('test:', 0, best_coup)
    return 0
