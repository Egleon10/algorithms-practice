#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#hard

import json

nums1 = input('nums1 = ')
nums2 = input('nums2 = ')

nums1 = json.loads(nums1)
nums2 = json.loads(nums2)

nums = []
for i in nums1:
    nums.append(int(i))
for i in nums2:
    nums.append(int(i))

nums.sort()

a = len(nums) / 2
if a % 1 == 0:
    b = (nums[a] + nums[a + 1]) / 2
else:
    b = nums[int(a - 0.5)]

print(b)
