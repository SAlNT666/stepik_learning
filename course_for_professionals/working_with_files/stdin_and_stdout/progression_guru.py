from sys import stdin


def is_ap(nums):
    d_of_ap = nums[1] - nums[0]
    ap = (nums[0] + i * d_of_ap for i in range(len(nums)))
    for n in nums:
        if n != ap.__next__():
            return 0
    return 1


def is_gp(nums):
    d_of_gp = nums[1] / nums[0]
    gp = (nums[0] * d_of_gp ** i for i in range(len(nums)))
    for n in nums:
        if n != gp.__next__():
            return 0
    return 1


nums = [int(n) for n in stdin]
if is_ap(nums):
    print('Арифметическая прогрессия')
elif is_gp(nums):
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')
