import numpy as np


def compute_eigenvalues(matrix: np.ndarray):
    lambdas = np.poly(matrix)
    return np.roots(lambdas)


def compute_eigenvector(matrix: np.ndarray, eigenvalue: float):
    A = matrix - eigenvalue * np.eye(matrix.shape[0])
    _, _, V = np.linalg.svd(A)
    return V[-1, :]


def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues = compute_eigenvalues(matrix)
    eigenvectors = np.zeros((0, matrix.shape[0]))
    for i in range(len(eigenvalues)):
        eigenvector = compute_eigenvector(matrix, eigenvalues[i])
        eigenvectors = np.vstack((eigenvectors, eigenvector))
    return eigenvalues, eigenvectors.T


matrix = np.array([[3, 1, 2], [2, 4, 1], [1, 1, 5]])
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
print(f"Eigenvalues: {eigenvalues.round(2)}")
print(f"Eigenvectors:\n {eigenvectors.round(2)}")

# Expected output:
eig = np.linalg.eig(matrix)
print(f"Eigenvalues: {eig[0].round(2)}")
print(f"Eigenvectors:\n {eig[1].round(2)}")
