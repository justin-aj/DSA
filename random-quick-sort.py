# Approach 2: Quicksort using list comprehension
import random


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        print(arr, "arr")
        rand = random.randint(1, len(arr) - 2)
        pivot = arr[rand]
        print(rand, pivot, "OK")
        print(arr[:rand], arr[rand + 1:])
        left = [x for x in arr[:rand] + arr[rand + 1:] if x < pivot]
        right = [x for x in arr[:rand] + arr[rand + 1:] if x >= pivot]
        print(left, right)
        return quicksort(left) + [pivot] + quicksort(right)

# Example usage
arr = [1, 7, 4, 1, 10, 9, -2]
sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)