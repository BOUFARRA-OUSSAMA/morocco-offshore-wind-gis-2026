"""Fuzzy AHP weighting utilities."""
from typing import List
import numpy as np


def compute_fuzzy_weights(pairwise_matrix: np.ndarray) -> np.ndarray:
    """Compute fuzzy AHP weights from a pairwise comparison matrix."""
    # Placeholder: implement fuzzy AHP (e.g., Chang's extent analysis)
    eigvals, eigvecs = np.linalg.eig(pairwise_matrix)
    principal = np.argmax(eigvals.real)
    weights = eigvecs[:, principal].real
    weights = weights / weights.sum()
    return weights


def consistency_ratio(pairwise_matrix: np.ndarray) -> float:
    """Approximate consistency ratio for the matrix."""
    n = pairwise_matrix.shape[0]
    eigvals, _ = np.linalg.eig(pairwise_matrix)
    lambda_max = eigvals.real.max()
    ci = (lambda_max - n) / (n - 1)
    # Random index (RI) values for n=1..10; extend as needed
    ri_table = {1: 0.0, 2: 0.0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
    ri = ri_table.get(n, 1.49)
    return ci / ri if ri else 0.0
