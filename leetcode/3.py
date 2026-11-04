#Given a string s, find the length of the longest substring without duplicate characters.
#medium

s = str(input('s = '))
m = 0
a = ''

for i in s:
    if i not in a:
        a += i
    else:
        while i in a:
            a = a[1:]
        a += i

    m = max(m, len(a))

print(m)