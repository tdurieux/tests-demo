def find(nums):

    smallest = 9999
    highest = -9999

    for num in nums:
        if num < smallest:
            smallest = num
        if num > highest:
            highest = num
    return smallest, highest
