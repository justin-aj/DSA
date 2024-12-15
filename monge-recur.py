"""def monge_recur(arr, i, j, k, l):
    print(i, j, k, l, len(arr[0]))
    if i < j and k < l and arr[i][k] + arr[j][l] <= arr[i][l] + arr[j][k]:
        monge_recur(arr, i + 1, j + 1, k + 1, l + 1)
    else:
        return "Not a Monge array"

i = 0
j = 1
k = 0
l = 1
monge_recur(arr, i, j, k, l)"""
def monge_recur(arr, i=0, j=1, k=0, l=1):
    rows = len(arr[0])
    cols = len(arr[0])

    # Base case
    if i == rows - 1:
        return "The array is a Monge array"

    # Debug statement: print values being checked
    if i < j and k < l:
        print(f"Checking: arr[{i}][{k}]={arr[i][k]}, arr[{j}][{l}]={arr[j][l]}, arr[{i}][{l}]={arr[i][l]}, arr[{j}][{k}]={arr[j][k]}")
        if arr[i][k] + arr[j][l] > arr[i][l] + arr[j][k]:
            return f"Not a Monge array: Diagonal inequality failed at rows ({i},{j}) and cols ({k},{l})"

    # Move to the next set of columns
    if l < cols - 1:
        return monge_recur(arr, i, j, k, l + 1)
    elif k < cols - 2:
        return monge_recur(arr, i, j, k + 1, k + 2)

    # Move to the next pair of rows
    elif j < rows - 1:
        return monge_recur(arr, i, j + 1, 0, 1)
    elif i < rows - 2:
        return monge_recur(arr, i + 1, i + 2, 0, 1)
    return "Monge array"


# Example Monge array
arr = [[10, 17, 13, 28, 23],
       [17, 22, 16, 29, 23],
       [24, 28, 22, 34, 24],
       [11, 13, 6, 17, 7],
       [45, 44, 32, 37, 23],
       [36, 33, 19, 21, 6],
       [75, 66, 51, 53, 34]]

# Call the function
result = monge_recur(arr)
print(result)
