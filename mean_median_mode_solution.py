#! python3
from mesonbuild.utils.universal import exe_exists


# mean function
def mean_func(list_numbers, round_count):
    return round(sum(list_numbers) / len(list_numbers), round_count)


print(mean_func([1, 2, 11.78, 4, 12.2, 6, 7, 8, 9, 220], 3))


# median function
def median_func(list_numbers):
    sorted_nums = sorted(list_numbers)
    if len(list_numbers) % 2 == 0:
        return (
            sorted_nums[int(len(sorted_nums) / 2 - 1)],
            sorted_nums[int(len(sorted_nums) / 2)],
        )
    else:
        return sorted_nums[int(len(sorted_nums) / 2)]


print(median_func([1, 2, 3, 4, 5, 6, 7, 8]))


# mode function
def mode_func(list_numbers):
    count = {}
    for num in list_numbers:
        count.setdefault(num, 0)
        count[num] += 1
    return max(count, key=count.get)


print(mode_func([1, 1, 1, 3, 4, 4, 2, 4, 4, 4, 1]))
