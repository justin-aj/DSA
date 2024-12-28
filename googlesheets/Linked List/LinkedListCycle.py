class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = set()
        while head:
            if head in seen_nodes:  # Check if the node itself is already seen
                return True
            seen_nodes.add(head)  # Add the current node to the set
            head = head.next
        return False
