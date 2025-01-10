#! python 3
# a program to find the 2 numbers from a list of numbers that add up to a target number
# hash set method
# time complexity 0(n) - single iteration over the array
# auxiliary space - O(n) - space needed for hash set

numbers = [2, 7, 11, 15, 6, 98, 75, 3, 4, 87, 1, 8, 5]
target = 9

seen_dict = dict()

for num in numbers:
    # add the number to a hash set
    seen_dict[num] = numbers.index(num)
    # calculate the difference needed from curent num to target num
    diff = target - num
    # if the difference is already in the hash set we have a matching pair!
    if diff in seen_dict.keys():
        print(seen_dict[diff], numbers.index(num))
    else:
        continue