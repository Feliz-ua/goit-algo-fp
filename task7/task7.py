import random
from collections import Counter
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    sums = []
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sums.append(die1 + die2)
    return sums

def monte_carlo_probabilities(sums):
    count = Counter(sums)
    total = len(sums)
    probabilities = {s: count[s] / total for s in range(2, 13)}
    return probabilities

def analytical_probabilities():
    # Кількість способів отримати кожну суму
    ways = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]  # суми 2-12
    total_ways = 36
    probabilities = {s: w / total_ways for s, w in zip(range(2, 13), ways)}
    return probabilities

# Основна частина програми
num_rolls = 100000
sums = simulate_dice_rolls(num_rolls)
monte_carlo_probs = monte_carlo_probabilities(sums)
analytical_probs = analytical_probabilities()

# Вивід таблиці
print("Сума\tМонте-Карло\tАналітична")
for s in range(2, 13):
    print(f"{s}\t{monte_carlo_probs[s]:.4f}\t\t{analytical_probs[s]:.4f}")

# Побудова графіка
sums_list = list(range(2, 13))
monte_carlo_values = [monte_carlo_probs[s] for s in sums_list]
analytical_values = [analytical_probs[s] for s in sums_list]

plt.figure(figsize=(10, 6))
plt.plot(sums_list, monte_carlo_values, label='Монте-Карло', marker='o')
plt.plot(sums_list, analytical_values, label='Аналітична', marker='x')
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Ймовірність сум при киданні двох кубиків')
plt.legend()
plt.grid(True)
plt.show()
