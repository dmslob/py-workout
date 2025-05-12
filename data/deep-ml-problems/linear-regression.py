import numpy as np
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
