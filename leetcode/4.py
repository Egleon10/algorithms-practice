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

med = len(nums) // 2
if len(nums) % 2 == 0:
    b = (nums[med] + nums[med - 1])/2
else:
    med = int(med) + 1
    b = nums[med - 1]

print(b)
