import math


# Write a Python function that computes the output of the sigmoid activation function given an input value z.
# The function should return the output rounded to four decimal places.
# https://www.deep-ml.com/problems/22
# Reasoning:
# The sigmoid function is defined as σ(z) = 1 / (1 + exp(-z)).
# For z = 0, exp(-0) = 1, hence the output is 1 / (1 + 1) = 0.5.
def sigmoid(z: float) -> float:
    """
    Computes the output of the sigmoid activation function for a given input z.
    The sigmoid function is defined as:
    f(z) = 1 / (1 + e^(-z))
    Args:
    z: The input value (float).
    Returns:
    The output of the sigmoid function, rounded to four decimal places (float).
    """
    try:
        output = 1 / (1 + math.exp(-z))
        return round(output, 4)
    except OverflowError:
        if z < 0:
            return 0.0000
        else:
            return 1.0000
    except Exception as e:
        print(f"An error occurred: {e}")
        return float('nan')


# Test:
print(f"sigmoid(0) = {sigmoid(0)}")
print(f"sigmoid(2) = {sigmoid(2)}")
print(f"sigmoid(-1) = {sigmoid(-1)}")
print(f"sigmoid(10) = {sigmoid(10)}")
print(f"sigmoid(-10) = {sigmoid(-10)}")