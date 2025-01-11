#! python 3
# a program to find the 2 numbers from a list of numbers that add up to a target number and return their indexes
# hash set method
# time complexity 0(n) - single iteration over the array
# auxiliary space - O(n) - space needed for hash set
import cProfile
import timeit


def hashset_2_sum():
    numbers = [2, 7, 11, 15, 6, 98, 75, 3, 4, 87, 1, 8, 5]
    target = 9

    seen_dict = dict()

    for i, num in enumerate(numbers):
        # add the number and its index to the dictionary
        seen_dict[num] = i
        diff = target - num
        if diff in seen_dict.keys():
            return (seen_dict[diff], i)
        else:
            continue


cProfile.run("hashset_2_sum()")
print(timeit.timeit("hashset_2_sum()", globals=globals()))
