# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#easy

import json

s = input()
nums = json.loads(s)

target = float(input())

ex_nums = []

for i in range(len(nums)):
    ex_nums.append(target - nums[i])
    if ((target - nums[i]) == nums[i]):
        if nums.count(nums[i]) == 1:
            continue
        else:
            c = nums[i]
            nums.remove(nums[i])
            a = i
            b = nums.index(c + 1)
    if (target- nums[i]) in nums:
        a = nums.index(target- nums[i])
        b = i
        break

print('[' + str(a) + ',' + str(b) + ']')