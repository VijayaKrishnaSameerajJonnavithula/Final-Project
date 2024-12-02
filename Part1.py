import numpy as np
import time

# Create a large matrix
N = 1000
matrix = np.random.rand(N, N)

# Row-major order access
def row_major_sum(matrix):
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total

# Column-major order access
def column_major_sum(matrix):
    total = 0
    for col in range(matrix.shape[1]):
        for row in range(matrix.shape[0]):
            total += matrix[row][col]
    return total

# Measure performance
start_row = time.time()
row_sum = row_major_sum(matrix)
end_row = time.time()

start_col = time.time()
col_sum = column_major_sum(matrix)
end_col = time.time()

# Print results
print(f"Row-Major Sum: {row_sum}, Time: {end_row - start_row:.6f} seconds")
print(f"Column-Major Sum: {col_sum}, Time: {end_col - start_col:.6f} seconds")
