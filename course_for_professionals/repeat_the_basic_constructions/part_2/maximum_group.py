nums = list(range(int(input()) + 1))

nums_sum_dict = dict()
for i in nums:
    d_sum = sum(int(d) for d in str(i))
    nums_sum_dict[d_sum] = nums_sum_dict.get(d_sum, 0) + 1

print(max(nums_sum_dict.values()))
