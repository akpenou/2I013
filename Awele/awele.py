def init():
    plateau = [ [ 4 for x in range(6) ] for y in range(2) ]
    joueur = 1
    coups_possibles = list()
    coups_faits = list()
    score = [ 0 for i in range(2) ]
    jeu = [ plateau, joueur, coups_possibles, coups_faits, score ]
    return jeu

def game_over(jeu):
    plateau, joueur, coups_possibles, coups_faits, score = jeu
    return True if coups_possibles else False

def winner(jeu):
    plateau, joueur, coups_possibles, coups_faits, score = jeu
    j1, j2 = score
    if j1 > j2:
        return 1
    if j2 > j1:
        return 2
    return 0

def mapper_add(plateau, index, add = 0):
    index %= 8
    x = index if index < 4 else 3 - index % 4
    y = index / 4
    plateau[y][x] += add
    return plateau[y][x]


def mapper_drop(plateau, index, condition):
    index %= 8
    x = index if index < 4 else 3 - index % 4
    y = index / 4
    res = 0
    if condition(x, y):
        res = plateau[y][x]
        plateau[y][x] = 0
    return res


def play(jeu, coup):
    plateau, joueur, coups_possibles, coups_faits, score = jeu
    player_y, player_x = coup
    index = player_x + player_y * 4
    nb_graine = mapper(plateau, index)
    plateau[player_y][player_x] = 0
    res = 0
    for tmp_index in range(index + 1, index + nb_graine + 2):
        mapper_add(plateau, tmp_index, 1)
    condition = lambda x, y: y != joueur and plateau[y][x] in [2, 3]
    for tmp_index in range(index + 1, nb_graine + 1):
        graines = mapper_drop(plateau, tmp_index, condition)
        if not graines:
            break
        res += tmp
    score[joueur] += res

def get_coups(jeu):
    plateau, joueur, coups_possibles, coups_faits, score = jeu
    

