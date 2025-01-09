#! python 3
# a program to find the 2 numbers from a list of numbers that add up to a target number
# https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/


numbers = [2, 7, 11, 15]
target = 9

# naive approach with memoization optimization

# memoization dictionary
memory_dict = {}

for i in range(1, len(numbers) - 1):
    # print(i)
    for num in numbers:
        # if the key "numbers[i] + num* exists in memory dictionary
        # means we have already calculated it
        if (f"{numbers[i]} + {num}") in memory_dict.keys():
            continue
        else:
            # add the combination as a key and the sum and the number coordinates as a list in value
            memory_dict[f"{num} + {numbers[i]}"] = [
                num + numbers[i],
                i,
                numbers.index(num),
            ]
            # add the combination also in reverse as we have already calculated it
            memory_dict[f"{numbers[i]} + {num}"] = [
                num + numbers[i],
                i,
                numbers.index(num),
            ]
# loop trough the keys and values in the memory_dictionary
for key, value in memory_dict.items():
    # if the first index in the value list == target
    if value[0] == target:
        print(value[1], value[2])
print(memory_dict)

# hash set method
# time complexity 0(n) - single iteration over the array
# auxiliary space - O(n) - space needed for hash set
