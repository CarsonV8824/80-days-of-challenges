from math import comb

def pascal_triangle_solution(row:int) -> list[list[int]]:
    matrix = []
    for i in range(row + 1):
        row_list = []
        for j in range((i + 1)):
            row_list.append(comb(i, j))

        matrix.append(row_list)
    return matrix

print(pascal_triangle_solution(12))