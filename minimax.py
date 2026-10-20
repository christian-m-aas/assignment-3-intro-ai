import math


def minimax_search(game, state):
    player = game.to_move(state)  # alle verdier regnes fra denne spillerens ståsted

    def max_value(state):
        if game.is_terminal(state):
            return game.utility(state, player), None

        v = -math.inf
        move = None

        for action in game.actions(state):
            v2, _ = min_value(game.result(state, action))

            if v2 > v:  # MAX velger trekket med høyest verdi
                v = v2
                move = action

        return v, move

    def min_value(state):
        if game.is_terminal(state):
            return game.utility(state, player), None

        v = math.inf
        move = None

        for action in game.actions(state):
            v2, _ = max_value(game.result(state, action))

            if v2 < v:  # MIN velger trekket som er dårligst for oss
                v = v2
                move = action

        return v, move

    _, move = max_value(state)  # start med at det er vår tur (MAX)
    return move
