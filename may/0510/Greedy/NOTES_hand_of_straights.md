# Hand of Straights — Tough One ⚠️

This is a tricky greedy problem. Key things to remember:

## Pattern
Greedy + Min Heap + Hashmap

## Why it's hard
- Easy to overcomplicate (don't use a tuple in the heap)
- Heap stores unique values only — frequencies go in the hashmap
- Only pop from heap when `hashmap[heap[0]] == 0`
- If a middle value hits 0 but it's not the heap top → gap in sequence → return False

## Key checks
1. `if len(hand) % groupSize != 0` → return False immediately
2. Always start group from `heap[0]` (the current minimum)
3. Pop from heap only when count hits 0 AND it's the current top
