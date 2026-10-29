import math

def determinant(matrix: list[list[float|int]]) -> float:
	return ((matrix[0][0]*matrix[1][1]) - matrix[0][1]*matrix[1][0])

def trace(matrix: list[list[float|int]]) -> float:
	return (matrix[0][0] + matrix[1][1])

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	tr = trace(matrix)
	det = determinant(matrix)
	eigen_value1 = (tr + (math.sqrt(tr*tr - 4*det)))/2
	eigen_value2 = (tr - (math.sqrt(tr*tr - 4*det)))/2
	if (eigen_value1 >= eigen_value2):
		return [eigen_value1, eigen_value2]
	else:
		return [eigen_value2, eigen_value1]
	return eigenvalues