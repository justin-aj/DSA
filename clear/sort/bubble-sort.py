a = [43,5,6,2,1, 9, 19, 23]

for i in range(0,len(a)):
    print(0, len(a) - i - 1)
    print(a, "Before")
    for j in range(0, len(a) - i - 1):
        print(a[j], a[j+1], "Comparing")
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            print(a[j], a[j + 1], "Swapped", a)


print(a)