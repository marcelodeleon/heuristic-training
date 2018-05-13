from datetime import datetime
from adversarial_search.games.cuanteti import Cuanteti
from adversarial_search.agents.minimax import MiniMaxAgent
from adversarial_search.agents.random import RandomAgent
from adversarial_search.core import run_match


def cuanteti_heuristic(agent, game, depth):
    square_value = {'X': 1, 'O': -1, '.': 0}

    # List of weights optimized by an evolutive algorithm.
    # square_factors = [
    #     -0.7324115189707612,
    #     0.12078368821643881,
    #     0.24205561304424505,
    #     -0.3173240866627467,
    #     -0.5677844855700339,
    #     -0.1478569245925585,
    #     0.3188820972130644,
    #     -0.366474144603806,
    #     0.22821093817844829,
    #     0.7151181400263911,
    #     0.9617711404696707,
    #     0.2574752229095243,
    #     -0.19441311412969342,
    #     0.008356392573539262,
    #     0.2840565747869781,
    #     -0.8239491893617041
    # ]
    square_factors = [
        -0.12899457523522595,
        0.1899452948288034,
        0.2784343544516066,
        -0.2694401007690084,
        -0.5393115681552205,
        0.775375233487448,
        0.6002570361544448,
        -0.4167383677927503,
        -0.9815939162152347,
        0.9215688422576132,
        0.8840081488366216,
        0.27206191520509426,
        0.9115437223532235,
        0.603356682733569,
        0.11598483445763375,
        0.14563887834630718
    ]
    board_value = sum([square_value[s] * p for s, p in
                       zip(game.board, square_factors)])

    return board_value if agent.player == 'Xs' else -board_value


def run_test(agent1, agent2, matches=1000):
    """
    Test a heuristic function as agent1 against an agent2.
    """
    wins = 0
    draws = 0
    loses = 0

    for i in range(matches):
        result = run_match(Cuanteti(), agent1, agent2)[0]['Xs']

        if result > 0:
            wins += 1
        elif result == 0:
            draws += 1
        else:
            loses += 1

    for i in range(matches):
        result = run_match(Cuanteti(), agent2, agent1)[0]['Os']
        if result > 0:
            wins += 1
        elif result == 0:
            draws += 1
        else:
            loses += 1

    return wins, loses, draws


def print_title(title):
    print('-'*170)
    print('{:^90}'.format(title))
    print('-'*170)

if __name__ == '__main__':
    player = MiniMaxAgent(heuristic=cuanteti_heuristic)
    random = RandomAgent()
    random_minimax = MiniMaxAgent()

    # Number of matches played as 'X' and as 'O'.
    matches = 5000

    print_title('Minimax con heuristica optimizada vs. Random Agent.')
    print('{} {:>45} {:>45}'.format('Ganados', 'Perdidos', 'Empatados'))
    wins, loses, draws = run_test(player, random, matches)
    print('{:>35} {:>45} {:>45}'.format(wins, loses, draws))

    print_title('Minimax con heuristica optimizada vs. Minimax con heuristica aleatoria.')
    print('{} {:>45} {:>45}'.format('Ganados', 'Perdidos', 'Empatados'))
    wins2, loses2, draws2 = run_test(player, random_minimax, matches)
    print('{:>35} {:>45} {:>45}'.format(wins2, loses2, draws2))
