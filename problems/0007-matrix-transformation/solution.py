import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	
	A = np.array(A)
	T = np.array(T)
	S = np.array(S)

	try:
		if ((np.ndim(S) != 2)or(np.ndim(T) != 2)or(T.shape[0] != T.shape[1])or(S.shape[0] != S.shape[1])):
			return -1
		
		if ((np.linalg.matrix_rank(T) < T.shape[0])or(np.linalg.matrix_rank(S) < S.shape[0])):
			return -1

		Tinv = np.linalg.inv(T)
		transformed_matrix = Tinv @ A @ S
		return transformed_matrix
	except:
		return -1