import random
import secrets

fruits = ["apple", "banana", "cherry", "mango", "orange"]
random_fruit = random.choice(fruits)
print(f"Random fruit:{random_fruit}")
n = 3  # number of random items
random_3_fruits = random.sample(fruits, n)
print(f"Random 3 distinct fruits:{random_3_fruits}")


colors = ["red", "green", "blue", "yellow"]
random_color = colors[random.randint(0, len(colors) - 1)]
print(f"Random color:{random_color}")


numbers = [10, 20, 30, 40, 50]
random_number = secrets.choice(numbers)
print(f"Random secure number:{random_number}")

numbers = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(numbers)
n = 3
random_numbers = numbers[:n]
print(f"Random distinct numbers:{random_numbers}")
