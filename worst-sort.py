a = [3,5,6,2,1, 9, 19, 23]

for i in range(0,len(a)):
    for j in range(i, len(a)):
        print(a[j],a[i])
        while a[j] < a[i]:
            a[i], a[j] = a[j], a[i]
            print(a[j], a[i], "Swapped")


print(a)