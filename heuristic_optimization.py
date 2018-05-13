import random
import numpy
from deap import base, creator, tools, algorithms
from adversarial_search.agents.minimax import MiniMaxAgent
from adversarial_search.agents.random import RandomAgent
from adversarial_search.games.cuanteti import Cuanteti
from adversarial_search.core import run_match

# Each individual will have a length of 16, as there are 16 boxes in quanteti
# board.
IND_SIZE = 16

# type
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# initialization
toolbox = base.Toolbox()
toolbox.register("attribute", random.uniform, -1, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attribute, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def evaluate(individual):
    def cuanteti_heuristic(agent, game, depth):
        square_value = {'X': 1, 'O': -1, '.': 0}
        square_factors = individual
        board_value = sum([square_value[s] * p for s, p in
                           zip(game.board, square_factors)])

        return board_value if agent.player == 'Xs' else -board_value

    # Amount of matches played as 'X' and as 'O'.
    matches = 50
    wins = 0
    agent1 = MiniMaxAgent(heuristic=cuanteti_heuristic)
    agent2 = RandomAgent()

    for i in range(matches):
        result = run_match(Cuanteti(), agent1, agent2)
        if result[0]['Xs'] > 0:
            wins += 1

    for i in range(matches):
        result = run_match(Cuanteti(), agent2, agent1)
        if result[0]['Os'] > 0:
            wins += 1

    return wins,

# Define genetic operators.
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)


def evolution():
    # create population
    pop = toolbox.population(n=100)
    CXPB, MUTPB, NGEN = 0.5, 0.2, 10

    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=CXPB, mutpb=MUTPB,
                                   ngen=NGEN, stats=stats, halloffame=hof,
                                   verbose=True)

    return hof.items[0]


if __name__ == "__main__":
    best = evolution()
    print('Solution:')
    print(best)
