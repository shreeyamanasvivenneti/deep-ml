import numpy as np

def flatten_matrix(matrix: list[list[int|float]]) -> list[int|float]:
	m = len(matrix)
	if (m == 0):
		return []
	n = len(matrix[0])
	vector = []
	for i in range(m):
		for j in range(n):
			vector.append(matrix[i][j])
	return vector

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	vector = flatten_matrix(a)
	if (len(vector) == 0):
		return []
	m = new_shape[0]
	n = new_shape[1]
	if (m*n != len(a)*len(a[0])):
		return []
	mn = len(vector)
	reshaped_matrix = []
	row = []
	for i in range(mn):
		row.append(vector[i])
		if ((i+1) % n == 0):
			reshaped_matrix.append(row)
			row = []
	return reshaped_matrix