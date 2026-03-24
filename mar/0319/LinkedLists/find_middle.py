# Find Middle of Linked List
# Pattern: Slow/Fast pointers
# Difficulty: Easy

def findMiddle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
