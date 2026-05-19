from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    summ = 0
    for num in nums:
        summ += num

    return summ

def get_min(nums: List[int]) -> int:
    minn = nums[0]
    for num in nums:
        if num < minn:
            minn = num

    return minn

def get_max(nums: List[int]) -> int:
    maxx = 0
    for num in nums:
        if num > maxx:
            maxx = num

    return maxx

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
