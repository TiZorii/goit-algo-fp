import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    outcomes = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        roll = random.randint(1, 6) + random.randint(1, 6)
        outcomes[roll] += 1

    for key in outcomes:
        outcomes[key] /= num_rolls

    return outcomes

def plot_probabilities(outcomes):
    sums = list(outcomes.keys())
    probabilities = list(outcomes.values())

    plt.bar(sums, probabilities, tick_label=sums)
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум двох кидків кубиків')
    plt.show()

# Приклад використання
num_rolls = 10000
outcomes = simulate_dice_rolls(num_rolls)
print(outcomes)
plot_probabilities(outcomes)
