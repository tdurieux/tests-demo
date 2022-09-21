def find(nums):
    if len(nums) == 0:
        return None, None

    smallest = 9999
    highest = -9999

    for num in nums:
        if num < smallest:
            smallest = num
        if num > highest:
            highest = num
    return smallest, highest
