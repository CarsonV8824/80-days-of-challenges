from math import comb

def pascal_triangle_solution(row):
    my_list = []
    
    for i in range(row):
        row_list = []
        for i in range(col := (row + 1)):
            row_list.append(comb(row, col))
        my_list.append(row_list)

    return my_list

print(pascal_triangle_solution(4))