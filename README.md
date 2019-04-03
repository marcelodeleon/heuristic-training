# Heuristic Optimization
The goal of the algorithm is to train an agent –by optimizing it's heuristic– to play "Cuanteti", 
a custom variant of the game of "Tateti". An evolutive algorithm will be used to optimize the parameters
of the heuristics. The **Minimax** player using such heuristic should win most matches against a **Minimax**
player with a random heuristic.

## Heuristic Model
The model is based in giving a weight(Ω) to each cell of the board depending on what's currently
inside it ('X', 'O' or empty).
The weights are floating point values within the range [-1.0, 1.0].

Each cell value is calculated as:
  * 1 * Ω If the cell is ocupied by the active player.
  * -1 * Ω If the cell is ocupied by the adversary.
  * 0 If the cell is empty.

## Optimization Strategy
The heuristic parameters will be optimized using the _deap_ Python library, through a genetic algorithm.

### Individual
Each individual will be represented as a vector of weights(Ω), one for each cell of the board.

### Evaluation
To evaluate the fitness of an individual 100 games of Cuanteti will be player against a Random agent.
Playing against a smarter opponent like a Minimax player with random heuristics is too costly.
When evaluating, the player will play half of the matches as 'X' and the other half as 'Y'.

## Dependecies
Heuristic optimization developed in Python3.
Dependencies defined in requirements.txt

## Execute
Install dependencies (from project root):
```
pip3 install -r requirements.txt
```

Execute heuristic optimization (from project root):
```
python3 heuristic_optimization.py
```

Run a game between agents (from project root):
```
python3 run_cuanteti.py
```
