""" Starting at the bottom of an "infinite" staircase, you roll a single die
with the following rules:

- If rolled a 1 or 2: go down one step. 
- If rolled a 3, 4, or 5: go up one step.
- If rolled a 6: roll again and go up the resulting amount of steps.

This Random Walk simulation will accept a target floor, and will simulate
how many round of this game it would take you to reach that floor.
"""
import sys

import numpy as np

np.random.seed(438)  # Initialize random seed

random_walk = [0]  # Initianlize random walk

step = random_walk[-1]  # Start from initial point in our random walk series

# Accept first command-line argument or set to default of 60
target_step = int(sys.argv[1]) if len(sys.argv) > 1 else 60

while step < target_step:
    result = np.random.randint(1,7)  # Roll die

    if result <= 2:
        step = max(0, step - 1)
    elif result <= 5:
        step += 1
    else:
        step += np.random.randint(1,7)

    random_walk.append(step)  # Add random step to our series

print("\nYou were able to reach step " + str(target_step) + " after " \
        + str(len(random_walk)) + " rounds!")

import matplotlib.pyplot as plt

plt.plot(random_walk)
plt.title('Infinite Staircase - A Random Walk Simulation')
plt.xlabel('Round')
plt.ylabel('Step')
plt.grid(True)
plt.show()

