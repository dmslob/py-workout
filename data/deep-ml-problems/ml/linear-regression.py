import numpy as np

# https://www.deep-ml.com/problems/14
# Function that performs linear regression using the normal equation.
# The function should take a matrix X (features) and a vector y (target) as input,
# and return the coefficients of the linear regression model.
# Round your answer to four decimal places, -0.0 is a valid result for rounding a very small number.


def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    """
    Performs linear regression using the normal equation with NumPy.
    Parameters:
    X (list of lists): Feature matrix (each row is an observation, each column a feature).
    y (list): Target vector.
    Returns:
    list: Coefficients (theta) of the linear regression model, rounded to 4 decimal places.
    """
    X_transpose = np.transpose(X)
    X_transpose_X = np.dot(X_transpose, X)
    X_transpose_y = np.dot(X_transpose, y)
    try:
        theta = np.linalg.solve(X_transpose_X, X_transpose_y)
        return [round(val, 4) for val in theta]
    except np.linalg.LinAlgError:
        return None


# Test Case 1:
X1 = [[1, 1], [1, 2], [1, 3]]
y1 = [1, 2, 3]
# Expected: [0.0, 1.0]
print("Coefficients:", linear_regression_normal_equation(X1, y1))

# Test Case 2:
X1 = [[1, 3, 4], [1, 2, 5], [1, 3, 2]]
y1 = [1, 2, 1]
# Expected: [4.0, -1.0, -0.0]
print("Coefficients:", linear_regression_normal_equation(X1, y1))


# https://www.deep-ml.com/problems/15
# Function that performs linear regression using gradient descent.
# The function should take NumPy arrays X (features with a column of ones for the intercept)
# and y (target) as input, along with learning rate alpha and the number of iterations,
# and return the coefficients of the linear regression model as a NumPy array.
# Round your answer to four decimal places.
# -0.0 is a valid result for rounding a very small number.
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Performs linear regression using gradient descent.
    Parameters:
    X (numpy.ndarray): Feature matrix (with intercept column of ones).
    y (numpy.ndarray): Target vector.
    alpha (float): Learning rate.
    iterations (int): Number of iterations.
    Returns:
    numpy.ndarray: Coefficients of the linear regression model, rounded to 4 decimal places.
    """
    m, n = X.shape
    theta = np.zeros((n, 1))  # Initialize coefficients
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    for _ in range(iterations):
        gradient = (1 / m) * X.T.dot(X.dot(theta) - y)
        theta -= alpha * gradient
    return np.round(theta.flatten(), 4)  # Flatten to 1D array and round


# Test
X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
alpha = 0.01
iterations = 1000
print(linear_regression_gradient_descent(X, y, alpha, iterations))
