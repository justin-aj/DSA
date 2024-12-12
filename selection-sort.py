a = [9001,5,1110,30,0]


## Sorting in Desc
for j in range(0,len(a)):
    highest = a[j]
    index = j
    for i in range(j, len(a) - 1):
        if highest > a[i + 1]:
            pass
        else:
            index = i + 1
            highest = a[i + 1]
    if a[index] > a[j]:
        a[index], a[j] = a[j], a[index]

print(a)
# Sorting in Asc
for j in range(0,len(a)):
    lowest = a[j]
    index = j
    for i in range(j, len(a) - 1):
        if lowest > a[i + 1]:
            index = i + 1
            lowest = a[i + 1]
        else:
            pass
    if a[index] < a[j]:
        a[index], a[j] = a[j], a[index]

print(a)

