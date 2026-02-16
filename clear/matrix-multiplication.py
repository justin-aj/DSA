a = [[4, 5], [1, 2]]

# [[4, 5]] [[2, 4]]
# [[1, 2]] [[1, 3]]

b = [[2, 4], [1, 3]]

# c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0] #i = 0,j = 0, k = 0, 1
# c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1] #i = 0,j = 1, k = 0, 1
# c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0] #i = 1,j = 0, k = 0, 1
# c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1] #i = 1,j = 1, k = 0, 1

c = []
d = []
temp = 0

for i in range(len(a[0])):
    for j in range(len(b[0])):
        for k in range(len(a[0])):
            temp += a[i][k] * b[k][j]
        c.append(temp)
        temp = 0
    d.append(c)
    c = []
print(d)

def matrix_multiplication(a,b, result, i, j, k):
    k = 0
    result[i][j] += a[i][k] * b[k][j]
    result[i][j] += a[i][k + 1] * b[k + 1][j]
    if i != len(a[0]):
        i = i + 1
    if i < len(a[0]):
        return matrix_multiplication(a, b, result, i, j, k)
    if j != len(b[0]):
        j = j + 1
    if j < len(b[0]):
        i = 0
        return matrix_multiplication(a, b, result, i, j, k)
    return result

result = [[0 for j in range(len(b[0]))] for i in range(len(a))]
x = 0
y = 0
z = 0
print(matrix_multiplication(a,b, result, x, y, z))

result = [[0 for j in range(len(b[0]))] for i in range(len(a))]

def multiply(a, b, result, i, j, k):
    if i >= len(a):
        return
    if j >= len(b[0]):
        return multiply(a, b, result, i + 1, 0, 0)
    if k >= len(b):
        return multiply(a, b, result, i, j + 1, 0)
    result[i][j] += a[i][k] * b[k][j]
    multiply(a, b, result, i, j, k + 1)
    return result


# perform matrix multiplication
print(multiply(a, b, result, 0, 0, 0))

"""def recursive_loops(depth, max_depth, ranges, current=[]):
    print(depth, max_depth, ranges, current, "start")
    if depth == max_depth:
        # Base case: process the combination
        print(current, "current")  # Replace with your desired operation
        return

    # Iterate over the range for the current "loop"
    print(ranges[depth], "check")
    for i in range(ranges[depth]):
        # Add the current value to the combination and recurse
        print(i, "loop", current)
        recursive_loops(depth + 1, max_depth, ranges, current + [i])

# Example usage: equivalent to 3 nested loops
ranges = [2, 2, 2]  # Length of each loop (n, m, p)
recursive_loops(0, len(ranges), ranges)"""
