#! python 3
# a program to visualize Sierpinski Pascal triangle

import turtle


def get_midpoint(point_1, point_2):
    # point consists of x,y coordinates
    # return midpoint between two points
    return ((point_1[0] + point_2[0]) / 2), ((point_1[1] + point_2[1]) / 2)


def draw_sierpinski(points, depth):
    # Draw BIG triangle with the points provided
    turtle.penup()
    turtle.goto(points[0][0], points[0][1])
    turtle.pendown()
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])

    # If depth is greater than 0, recursively draw smaller triangles
    if depth > 0:
        draw_sierpinski(
            [
                points[0],
                get_midpoint(points[0], points[1]),
                get_midpoint(points[0], points[2]),
            ],
            depth - 1,
        )
        draw_sierpinski(
            [
                points[1],
                get_midpoint(points[0], points[1]),
                get_midpoint(points[1], points[2]),
            ],
            depth - 1,
        )
        draw_sierpinski(
            [
                points[2],
                get_midpoint(points[2], points[1]),
                get_midpoint(points[0], points[2]),
            ],
            depth - 1,
        )


# Initial triangle points
points = [[-200, -100], [0, 200], [200, -100]]

# Set the recursion depth
depth = 5

turtle.speed(0)  # Fastest speed
draw_sierpinski(points, depth)
turtle.done()
"""
import math

depth = 8
field_array = []

for i in range(0, depth):
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
    # print(index_left_x)
    # print(-index_left_x - 1)
    field_array[i][-index_left_x - 1] = 1

field_array.append([1 for i in range(0, depth + 1)])
for row in field_array:
    print(row)

print("\n")

for x in range(1, depth):
    for y in range(1, (len(field_array[x]) - 2)):
        field_array[x][y + 1] = field_array[x - 1][y + 1] + field_array[x - 1][y]
        # print(field_array[x])

for row in field_array:
    print(row)
"""
