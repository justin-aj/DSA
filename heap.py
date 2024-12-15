import heapq

a = [2, 4, 2, 3, 9]

heapq.heapify(a)

print(a)

heapq.heappush(a, 1)

print(a)

smallest = heapq.heappop(a)

print(smallest, a)

heapq.heappushpop(a, 1)

print(a)

heapq.heapreplace(a, 8)

print(a)

print(heapq.nlargest(2, a))

print(heapq.nsmallest(2, a))

max_heap = [-x for x in a]

heapq.heapify(max_heap)

print([-x for x in max_heap])


