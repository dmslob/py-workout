import numpy as np


def shuffle_data(X, y, seed=None):
    """
    https://www.deep-ml.com/problems/29
    Randomly shuffles two NumPy arrays, X and y, while maintaining the
    corresponding order between them.
    This function is particularly useful for shuffling datasets where X represents
    the features and y represents the labels, ensuring that each feature vector
    remains paired with its correct label after shuffling.
    Args:
        X (np.ndarray): The first array (e.g., features) to be shuffled.
        y (np.ndarray): The second array (e.g., labels) to be shuffled.
        seed (int, optional): A seed for the random number generator to ensure
                              reproducibility of the shuffle. Defaults to None.

    Returns:
        tuple[np.ndarray, np.ndarray]: A tuple containing the shuffled arrays,
                                        (X_shuffled, y_shuffled).
    """
    if seed is not None:
        np.random.seed(seed)
    # Get the number of samples
    n_samples = X.shape[0]
    # Generate a random permutation of indices from 0 to n_samples-1
    permutation = np.random.permutation(n_samples)
    # Use the same permutation to shuffle both arrays
    x_shuffled = X[permutation]
    y_shuffled = y[permutation]

    return x_shuffled, y_shuffled


print(shuffle_data(
    np.array([[1, 2], [3, 4], [5, 6], [7, 8]]),
    np.array([1, 2, 3, 4]),
    seed=42))

print(shuffle_data(
    np.array([[1, 1], [2, 2], [3, 3], [4, 4]]),
    np.array([10, 20, 30, 40]),
    seed=24))
