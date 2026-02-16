def insertion_sort_divide_conquer(arr):
    print(arr,"start")
    # Base case: if the list has one or no elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Divide: Separate the last element from the rest of the array
    last_element = arr[-1]
    print(last_element, arr[:-1])
    rest_sorted = insertion_sort_divide_conquer(arr[:-1])  # Sort the rest of the array recursively
    print(rest_sorted, "HERE")

    # Conquer: Insert the last element into the sorted part of the array
    i = len(rest_sorted) - 1

    print(i, rest_sorted[i], last_element, "OK")
    # Find the correct position for the last_element
    while i >= 0 and rest_sorted[i] > last_element:
        i -= 1

    # Insert the last element into its correct position
    print(rest_sorted[:i + 1] + [last_element] + rest_sorted[i + 1:], "end")
    return rest_sorted[:i + 1] + [last_element] + rest_sorted[i + 1:]

# Example usage
arr = [4, 3, 5, 1, 2]
sorted_arr = insertion_sort_divide_conquer(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5]
