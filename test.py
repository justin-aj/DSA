
a = [1, 3, 4, 2]

for i in range(len(a)):
    print(i , a[i])

for i, j in enumerate(a):
    print(i, j)

# Both are same

from bisect import bisect_left, bisect_right, insort, insort_left, insort_right

a = [1, 5, 2, 2]
e = 5

res = bisect_left(a, e)
print(res)

res = bisect_right(a, e)
print(res)

insort_left(a, e)
print(a)

insort_right(a, e)
print(a)

