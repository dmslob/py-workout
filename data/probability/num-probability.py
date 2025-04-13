import random
import matplotlib.pyplot as plt

total_flips = 0
numerical_probability = []
H_count = 0

for i in range(0, 5000):
    new_flip = random.choice(['H', 'T'])
    total_flips += 1
    if new_flip == 'H':
        H_count += 1
    numerical_probability.append(H_count / total_flips)

plt.figure(figsize=(10, 6))
plt.plot(numerical_probability, label='Numerical probability of heads')
plt.axhline(y=0.5, color='r', linestyle='-', label='Expected value (0.5)')
plt.xlabel("Number of toss")
plt.ylabel("Numerical probability of heads")
plt.title("Law of Large Numbers: Coin Toss")
plt.legend()

plt.show()
