#! python3
# a program that prints oout multiplication table 1 - 9
from tomlkit import string

multiplication_range = int(input("Please enter the desired multiplication range"))

# set up the 2D array / list of lists
multiplication_table = [[] for x in range(multiplication_range)]

# populate the lists inside main list with a double for loop 1x1 1x2 1x3 etc
for i in range(1, multiplication_range + 1):
    for j in range(1, multiplication_range + 1):
        multiplication_table[i - 1].append(i * j)

# determine the widest numeric value in the very bottom of the table aka the highest values
column_widths = [len(str(i)) for i in multiplication_table[-1]]

print(column_widths)

for i in range(0, multiplication_range):
    row_adjusted = str()
    for num in multiplication_table[i]:
        string_num = str(num)
        # print(f"current column is {column_widths[i]} wide")
        # print(f"number is {string_num}, {len(string_num)} wide")
        if len(string_num) == column_widths[i]:
            row_adjusted += " " + string_num
            # row_adjusted += string_num.rjust(len(string_num) + 1, " ")
            # print(f"dont need to adjust {string_num}!")
        if len(string_num) < column_widths[i]:
            # print(
            #    f"adjust {string_num} by {column_widths[i] - len(string_num)} because {column_widths[i]} is larger"
            # )
            row_adjusted += " " + string_num.rjust(
                column_widths[i] - len(string_num), "x"
            )

        else:
            print(f"somethings wrong with {len(string_num)} and {column_widths[i]}!")
    print(row_adjusted)
