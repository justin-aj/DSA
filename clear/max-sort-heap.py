heap_list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

def heap_sort(heap_list):
    def max_heapify(arr, n, i):
        print(arr, n, i, "Heap")
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Compare left child
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Compare right child
        if right < n and arr[right] > arr[largest]:
            largest = right

        # Swap and continue heapifying if root is not the largest
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            max_heapify(arr, n, largest)

    n = len(heap_list)

    # Step 1: Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(heap_list, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        print(heap_list[i], heap_list[0])
        print(heap_list, "before")
        # Swap the root (max element) with the last element
        heap_list[i], heap_list[0] = heap_list[0], heap_list[i]
        # Call max_heapify on the reduced heap
        print(heap_list, "after")
        max_heapify(heap_list, i, 0)

# Perform heap sort
heap_sort(heap_list)

print("Sorted list:", heap_list)
