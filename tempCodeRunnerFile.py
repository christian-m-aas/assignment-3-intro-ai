import math

State = tuple[int, list[str | int]]
Action = str | int


class Game:
    def initial_state(self) -> State:
        return 0, ['A', 'B', 'C']

    def to_move(self, state: State) -> int:
        player, _ = state
        return player

    def actions(self, state: State) -> list[Action]:
        _, actions = state
        return actions

    def result(self, state: State, action: Action) -> State:
        if action == 'A':
            return (self.to_move(state) + 1) % 2, [-50, 50]
        elif action == 'B':
            return (self.to_move(state) + 1) % 2, [3, 1]
        elif action == 'C':
            return (self.to_move(state) + 1) % 2, [-5, 15]
        assert type(action) is int
        return (self.to_move(state) + 1) % 2, [action]

    def is_terminal(self, state: State) -> bool:
        _, actions = state
        return len(actions) == 1

    def utility(self, state: State, player: int) -> float:
        assert self.is_terminal(state)
        _, actions = state
        assert type(actions[0]) is int
        return actions[0] if player == self.to_move(state) else -actions[0]

    def print(self, state):
        print(f'The state is {state} and ', end='')
        if self.is_terminal(state):
            print(f'P1\'s utility is {self.utility(state, 0)}')
        else:
            print(f'it is P{self.to_move(state)+1}\'s turn')


def minimax_search(game: Game, state: State) -> Action | None:
    player = game.to_move(state)

    def max_value(state: State) -> tuple[float, Action | None]:
        if game.is_terminal(state):
            return game.utility(state, player), None

        v = -math.inf
        move = None

        for action in game.actions(state):
            v2, _ = min_value(game.result(state, action))

            if v2 > v:
                v = v2
                move = action

        return v, move

    def min_value(state: State) -> tuple[float, Action | None]:
        if game.is_terminal(state):
            return game.utility(state, player), None

        v = math.inf
        move = None

        for action in game.actions(state):
            v2, _ = max_value(game.result(state, action))

            if v2 < v:
                v = v2
                move = action

        return v, move

    value, move = max_value(state)
    return move