def binary_search(numbers, target):
    if len(numbers) == 0:
        return None

    start_index = 0
    end_index = len(numbers)

    while start_index < end_index:
        middle_index = (start_index + end_index) // 2
        if numbers[middle_index] == target:
            print(f'{target} found at index {middle_index}')
            return middle_index
        elif numbers[middle_index] > target:
            end_index = middle_index - 1
            start_index = 0
        elif numbers[middle_index] < target:
            start_index = middle_index + 1
            end_index = len(numbers)
    else:
        print(f'{target} not found!')
        return None


print(binary_search([1,2,3,5,6,7,11,16], 19))