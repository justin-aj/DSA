import heapq

print("Using Heapq")
# Creating a priority queue
pq = []

# Adding elements with priorities
heapq.heappush(pq, (3, "Task 1"))  # Priority 3
heapq.heappush(pq, (1, "Task 2"))  # Priority 1
heapq.heappush(pq, (2, "Task 3"))  # Priority 2

print(pq)

lar = max(pq, key=lambda x: x[0])

print(lar)

# Removing elements based on priority (smallest first)
while pq:
    priority, task = heapq.heappop(pq)
    print(f"Priority: {priority}, Task: {task}")


print("Using Priority Queue")

from queue import PriorityQueue

# Create a priority queue
pq = PriorityQueue()

# Adding elements
pq.put((3, "Task 1"))  # Priority 3
pq.put((1, "Task 2"))  # Priority 1
pq.put((2, "Task 3"))  # Priority 2

# Removing elements based on priority
while not pq.empty():
    priority, task = pq.get()
    print(f"Priority: {priority}, Task: {task}")

