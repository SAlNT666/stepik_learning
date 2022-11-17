nums = [int(i) for i in input().split()]
for i in list(set(nums)):
    nums.remove(i)
print(*sorted(set(nums)))
