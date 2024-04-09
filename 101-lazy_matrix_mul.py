#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a: First matrix (list of lists of integers or floats).
        m_b: Second matrix (list of lists of integers or floats).

    """
    # Convert lists to NumPy arrays
    np_m_a = np.array(m_a)
    np_m_b = np.array(m_b)

    # Validate m_a and m_b
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be lists of lists")
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a) or len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_a and m_b cannot be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a and m_b should contain only integers or floats")
    if len(set(len(row) for row in m_a)) > 1 or len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_a and m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b cannot be multiplied")

    # Perform matrix multiplication using NumPy
    result = np.dot(np_m_a, np_m_b)

    # Convert result back to list of lists
    result_list = result.tolist()

    return result_list
