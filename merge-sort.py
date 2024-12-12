a = [6,25,21,1,5,6, 14, 5,2,1,5]


#print(a[0:int(len(a)/2)], a[int(len(a)/2):])
#b = a[0:int(len(a)/2)]
#c = a[int(len(a)/2):]
#print(b[0:int(len(b)/2)], b[int(len(b)/2):])
#print(c[0:int(len(c)/2)], c[int(len(c)/2):])

# Ascending Order
def merge(a):
    if len(a) == 1:
        return a
    if len(a) == 2:
        if a[0] > a[1]:
            a[0], a[1] = a[1], a[0]
        return a
    b = merge(a[0:int(len(a)/2)])
    c = merge(a[int(len(a)/2):])
    d = []
    i, j = 0, 0
    while i < len(b) and j < len(c):
        if b[i] < c[j]:
            d.append(b[i])
            i += 1
        else:
            d.append(c[j])
            j += 1

    while i < len(b):
        d.append(b[i])
        i += 1

    while j < len(c):
        d.append(c[j])
        j += 1
    return d

print(merge(a))

# Descending Order
def merge(a):
    if len(a) == 1:
        return a
    if len(a) == 2:
        if a[0] < a[1]:
            a[0], a[1] = a[1], a[0]
        return a
    b = merge(a[0:int(len(a)/2)])
    c = merge(a[int(len(a)/2):])

    d = []
    i, j = 0, 0
    while i < len(b) and j < len(c):
        if b[i] > c[j]:
            d.append(b[i])
            i += 1
        else:
            d.append(c[j])
            j += 1

    while i < len(b):
        d.append(b[i])
        i += 1

    while j < len(c):
        d.append(c[j])
        j += 1

    return d

print(merge(a))