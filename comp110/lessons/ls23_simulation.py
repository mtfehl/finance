"""Example of stochastic simulation!

Goal: Find relative probabilities of a rolled pair
of dice summing to a given result.

To avoid some typing errors with matlablib/pyplot,
use basic instead of strict type checking:

File > Preferences > Settings...

Search for Python Type Checking. Change to basic.
"""

from typing import List
from random import randint
from matplotlib import pyplot

TRIALS: int = 321206
MAX_ROLL: int = 12


def main() -> None:
    """Entry point of the simulation."""
    # Simulate N Trials
    results: List[int] = simulate(TRIALS)
    # Count the outcomes of the trials
    counts: List[int] = count(results)
    # Plot the distribution
    plot(counts)


def simulate(n: int) -> List[int]:
    """Roll a pair of die n times and return a list of summed rolls."""
    rolls: List[int] = []
    # Loop n times and each iteration:
    for trial in range(0, n):
        # 1. roll a pair of die
        roll: int = randint(1, 6) + randint(1, 6)
        # 2. keep track of the results
        rolls.append(roll)
   
    return rolls


def count(results: List[int]) -> List[int]:
    # Establish an empty list for keeping 
    #   tallies on each possible result.
    counts: List[int] = []
    for i in range(0, MAX_ROLL + 1):
        counts.append(0)

    # Iterate through each result and 
    #   include its outcome in the tallied
    #   counts.
    for result in results:
        counts[result] += 1

    return counts


def plot(counts: List[int]) -> None:
    """Plot the results of our simualted experiment in a histogram."""
    pyplot.title("Distribution of Rolled Values.")
    pyplot.xlabel("Sum of Roll")
    pyplot.ylabel("Frequency")
    xaxis_value: range = range(0, MAX_ROLL + 1)
    pyplot.bar(xaxis_value, counts)
    pyplot.show()


if __name__ == "__main__":
    main()