heap_list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

def sort_heap(heap_list):
    def max_heapify(heap_list, i):
        largest = i
        left = (2 * i) + 1
        right = (2 * i) + 2
        if left < len(heap_list) and heap_list[left] > heap_list[largest]:
            largest = left
        if right < len(heap_list) and heap_list[right] > heap_list[largest]:
            largest = right
        if largest != i:
            heap_list[i], heap_list[largest] = heap_list[largest], heap_list[i]
            max_heapify(heap_list, largest)

    for i in range(len(heap_list) // 2 - 1, -1, -1):
        max_heapify(heap_list, i)

    return heap_list

sorted_heap = []
for i in range(len(heap_list)):
    first_element = sort_heap(heap_list)[0]
    heap_list.remove(first_element)
    sorted_heap.append(first_element)

print(sorted_heap)
