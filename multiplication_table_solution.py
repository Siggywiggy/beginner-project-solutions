#! python3
# a program that prints out multiplication table

multiplication_range = int(input("Please enter the desired multiplication range\n"))

# set up the 2D array / list of lists
multiplication_table = [[] for x in range(multiplication_range)]

# populate the lists inside main list with a double for loop 1x1 1x2 1x3 etc
for i in range(1, multiplication_range + 1):
    for j in range(1, multiplication_range + 1):
        multiplication_table[i - 1].append(
            i * j
        )  # append the result of the multiplication of row*column to the correct "row" sublist

# determine the widest numeric value in the very bottom of the table aka the highest values
column_widths = [len(str(i)) for i in multiplication_table[-1]]

for i in range(0, multiplication_range):
    row_adjusted = str()
    for j in range(0, len(multiplication_table[i])):
        if (
                len(str(multiplication_table[i][j])) == column_widths[j]
        ):  # if the num is as wide as the widest column
            # print(
            #    f"do nothing, number is as wide as the widest column, column width is {column_widths[j]} and lenght of number is {len(str(multiplication_table[i][j]))}"
            # )
            row_adjusted += " " + str(
                multiplication_table[i][j]
            )  # concatenate an empty space and the string value of the number to the row string
        elif len(str(multiplication_table[i][j])) < column_widths[j]:
            # print(
            #    f"need to adjust the number, narrower then widest column , column width is {column_widths[j]} and lenght of number is {len(str(multiplication_table[i][j]))}"
            # )
            row_adjusted += " " + str(multiplication_table[i][j]).rjust(
                column_widths[j], " "
            )  # concatenate a whitespace to the front and .rjust to the width of the column
        else:
            print(
                f"something is wrong with {multiplication_table[i][j]} and {column_widths[j]}"
            )

    print(
        row_adjusted
    )  # print the newly concatenated string for the row in multiplication table
