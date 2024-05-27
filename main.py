from random import choice

matrix1 = [
    [4, 6],
    [7, 3]
]

matrix2 = [
    [0, 0, 6, 4],
    [0, 0, 7, 3],
    [5, 5, 0, 0],
    [7, 3, 0, 0]
]

matrix = matrix2
num_move = 100_000_000

arr_p = [0] * len(matrix)
state = choice([*range(len(matrix))])
for _ in range(num_move):
    state = choice([index for index, el in enumerate(matrix[state]) for _ in range(el)])
    arr_p[state] += 1

ans = [*map(lambda x: x / sum(arr_p), arr_p)]
print(ans)
