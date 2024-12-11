a = [6,5,21,1,5]

for j in range(1, len(a)):
    temp = a[j - 1]
    print(j, "loops")
    while temp > a[j] and j != 0:
        print("loop start")
        print(j, temp, a[j], a)
        a[j-1] = a[j]
        a[j] = temp
        j = j - 1
        temp = a[j - 1]
        print(j, temp, a[j], a)

print(a)
