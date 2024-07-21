import numpy as np


def computeVectorLength(vector: np.ndarray) -> float:
    return np.sqrt(np.sum(vector**2))


def computeDotProduct(vector1: np.ndarray, vector2: np.ndarray) -> float:
    return np.dot(vector1, vector2)


def matrix_multi_vector(matrix: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return np.dot(matrix, vector)


def matrix_multi_matrix(
        matrix1: np.ndarray,
        matrix2: np.ndarray) -> np.ndarray:
    return np.dot(matrix1, matrix2)


def inverse_matrix(matrix: np.ndarray) -> np.ndarray:
    if (matrix.shape[0] != matrix.shape[1] or matrix.shape[0] != 2):
        print("Only 2x2 matrix is supported")
        return None

    det = matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    if det == 0:
        print("The matrix is not invertible")
        return None

    return np.array([[matrix[1, 1], -matrix[0, 1]],
                    [-matrix[1, 0], matrix[0, 0]]]) / det


def test():
    vector1 = np.array([1, 2])
    vector2 = np.array([3, 4])
    print(f"Vector1 length: {computeVectorLength(vector1)}")
    print(f"Vector1 dot Vector2:\n {computeDotProduct(vector1, vector2)}")
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[4, 3], [2, 1]])
    print(f"Matrix x Vector:\n {matrix_multi_vector(matrix1, vector1)}")
    print(f"Matrix1 x Matrix2:\n {matrix_multi_matrix(matrix1, matrix2)}")
    print(f"Inverse matrix:\n {inverse_matrix(matrix1)}")


test()
