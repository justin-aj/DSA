import heapq

priority_queue = [(1, "Task A"), (2, "Task B"), (3, "Task C")]

heapq.heapify(priority_queue)

print(priority_queue)

task = "Task C"

for i in range(len(priority_queue)):
    if priority_queue[i][1] == task:
        priority_queue.pop(i)
        break
    heapq.heapify(priority_queue)

heapq.heappush(priority_queue, (5, "Task C"))

print(priority_queue)

# Get the maximum key value by iterating
max_key = max(priority_queue, key=lambda x: x[0])
print("Max key:", max_key[0], "Task:", max_key[1])

