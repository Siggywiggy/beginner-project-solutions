#! python 3
# a program to find the 2 numbers from a list of numbers that add up to a target number and return their indexes
# hash set method
# time complexity 0(n) - single iteration over the array
# auxiliary space - O(n) - space needed for hash set
import cProfile
import timeit
import random

def hashset_2_sum():
    numbers = [random.randint(0,100) for num in range(20)]
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
