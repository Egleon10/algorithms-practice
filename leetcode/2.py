#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#medium

import json

s1 = input('l1 = ')
s2 = input('l2 = ')
l1 = json.loads(s1)
l2 = json.loads(s2)

ex_int1 = ''
ex_int2 = ''

for i in l1:
    ex_int1 = str(i) + ex_int1

for i in l2:
    ex_int2 = str(i) + ex_int2



number = str(int(ex_int1) + int(ex_int2))
ans = []

for i in range(len(number) - 1, -1, -1):
    ans.append(int(number[i]))

print(ans)