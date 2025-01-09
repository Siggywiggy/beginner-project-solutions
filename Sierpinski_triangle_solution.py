#! python 3
# a program to visualize Sierpinski Pascal triangle
import math

depth = 8

field_array = []

for i in range(0, depth + 1):
    # for every i need that i+1 numbers in a row
    # in every row total amount of indexes with 1-s are len(row)

    if i % 2 == 0:
        row = [0 for i in range(0, depth + 1)]
        field_array.append(row)
    elif i % 2 != 0:
        row = [0 for i in range(0, depth + 2)]
        field_array.append(row)

    index_left_x = math.floor((len(row) - i) / 2)

    field_array[i][index_left_x] = 1
    field_array[i][-index_left_x - 1] = 1

for row in field_array:
    print(row)