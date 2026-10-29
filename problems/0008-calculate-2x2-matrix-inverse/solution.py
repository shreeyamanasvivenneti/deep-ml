def determinant(matrix: list[list[float]]) -> float:
    """determinant is ad - bc"""
    return ((matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]))

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    if (determinant(matrix) == 0):
        return None
    detA = determinant(matrix)
    Ainv = [[matrix[1][1]/detA, -1*matrix[0][1]/detA], [-1*matrix[1][0]/detA, matrix[0][0]/detA]]
    return Ainv