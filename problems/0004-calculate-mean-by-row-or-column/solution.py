def calculate_matrix_mean_row(matrix: list[list[float]]) -> list[float]:
	if len(matrix) == 0:
		return [0]
	m = len(matrix)
	n = len(matrix[0])
	avg_vector = []
	for i in range(m):
		row_sum = 0
		for j in range(n):
			row_sum += matrix[i][j]
		row_avg = row_sum/n
		avg_vector.append(row_avg)
	return avg_vector

def calculate_matrix_mean_column(matrix: list[list[float]]) -> list[float]:
	if (len(matrix) == 0):
		return [0]
	m = len(matrix)
	n = len(matrix[0])
	avg_vector = []
	for j in range(n):
		col_avg = 0
		for i in range(m):
			col_avg += matrix[i][j]
		col_avg = col_avg/m
		avg_vector.append(col_avg)
	return avg_vector

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if (mode == "row"):
		return calculate_matrix_mean_row(matrix)
	else:
		return calculate_matrix_mean_column(matrix)
	return means