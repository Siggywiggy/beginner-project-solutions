def recursive_binary_search(nums, target, start_idx, end_idx):
    middle_index = (start_idx + end_idx) // 2

    if nums[middle_index] == target:
        return target, middle_index

    if len(nums) == 1 and nums[0] == target:
        return target, middle_index
    elif len(nums) == 1 and nums[0] != target:
        return None

    if target < nums[middle_index]:
        result = recursive_binary_search(nums, target, start_idx, middle_index - 1)
    elif target > nums[middle_index]:
        result = recursive_binary_search(nums, target, middle_index + 1, end_idx)

    return result


print(recursive_binary_search([1, 2, 3, 5, 6, 7, 11, 16], 3, 0, 7))