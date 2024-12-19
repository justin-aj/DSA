a = [4, 2, 2, 8, 3, 3, 1]

high = a[0]
low = a[0]

for i in a:
    if i > high:
        high = i
    if i < low:
        low = i

print(high, low)

c = []
for i in range(low, high+1):
    x = 0
    for j in a:
        if i == j:
            x += 1
    c.append(x)

print(c)

for i in range(1, len(c)):
    c[i] = c[i] + c[i - 1]

print(c)

output = [0, 0, 0, 0, 0, 0, 0]

for i in a[::-1]:
    output[c[i - low] - 1] = i
    c[i - low] -= 1

print(output, "out")