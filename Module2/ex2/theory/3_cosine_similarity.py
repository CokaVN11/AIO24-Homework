import numpy as np


def compute_cosine(vector1: np.ndarray, vector2: np.ndarray) -> float:
    return np.dot(vector1, vector2) / \
        (np.linalg.norm(vector1) * np.linalg.norm(vector2))


x = np.array([1, 2, 3, 4])
y = np.array([1, 0, 3, 0])

print(f"Cosine similarity: {np.round(compute_cosine(x, y), 2)}")
