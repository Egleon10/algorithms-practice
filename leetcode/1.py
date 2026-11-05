# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#easy

import json

s = input()
nums = json.loads(s)

target = float(input())

for i in range(len(nums)):
    need = target - nums[i]
    if need in nums[i + 1:]:
        a = i
        b = nums.index(need, i + 1)
        break

print('[' + str(a) + ',' + str(b) + ']')