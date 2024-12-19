from collections import deque

# Queue implementation using deque
queue = deque()

# Enqueue elements
queue.appendleft([1, 2])
queue.append(2)
queue.append(3)
queue.appendleft([1, 2])
print("Queue after enqueueing:", queue)  # Output: deque([1, 2, 3])

# Dequeue elements
print("Dequeued element:", queue.pop())  # Output: 1
print("Queue after dequeueing:", queue)  # Output: deque([2, 3])