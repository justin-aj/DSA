heap_list = [10, 5, 20, 2, 4, 8, 15]

def max_heapify(heap_list, i):
    largest = i
    left = (2 * i) + 1
    right = (2 * i) + 2
    if (2 * i) + 1 < len(heap_list):
        largest = left
    if (2 * i) + 2 < len(heap_list):
        largest = right
    if largest != i:
        if heap_list[i] < heap_list[left]:
            heap_list[i], heap_list[left] = heap_list[left], heap_list[i]
        elif heap_list[i] < heap_list[right]:
            heap_list[i], heap_list[right] = heap_list[right], heap_list[i]
        max_heapify(heap_list, largest)


for i in range(len(heap_list) // 2 - 1, -1, -1):
    max_heapify(heap_list, i)

print(heap_list)