def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if not a or not b:
		return -1

	m = len(b)
	result = []


	for row in a:
		if len(row) != m:
			return -1
		
		row_sum = sum(row[j]*b[j] for j in range(m))
		result.append(row_sum)
	
	return result
