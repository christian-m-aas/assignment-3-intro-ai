import math

def alpha_beta_search(game, state, depth_limit=None, eval_fn=None):
    
    player = game.to_move(state)  # alle verdier regnes fra denne spillerens ståsted

    def is_cutoff(state, depth):
        if game.is_terminal(state):
            return True
        return depth_limit is not None and depth >= depth_limit

    def evaluate(state):
        if game.is_terminal(state):
            return game.utility(state, player)
        return eval_fn(state, player)

    def max_value(state, alpha, beta, depth):
        if is_cutoff(state, depth):
            return evaluate(state), None
        v, move = -math.inf, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a), alpha, beta, depth + 1)
            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)
            if v >= beta:
                return v, move  # MIN har allerede et bedre alternativ høyere opp -> beskjær
        return v, move

    def min_value(state, alpha, beta, depth):
        if is_cutoff(state, depth):
            return evaluate(state), None
        v, move = math.inf, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a), alpha, beta, depth + 1)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha:
                return v, move  # MAX har allerede et bedre alternativ høyere opp -> beskjær
        return v, move

    _, move = max_value(state, -math.inf, math.inf, 0)
    return move

