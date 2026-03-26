# Top K Frequent Elements
# Pattern: Bucket Sort (3 loops problem)
# Difficulty: Medium

from collections import defaultdict

def topKFrequent(nums, k):
    # Step 1: count frequencies
    hash_map = defaultdict(int)
    for n in nums:
        hash_map[n] += 1

    # Step 2: bucket sort by frequency
    # index = frequency - 1
    li = [[] for _ in range(len(nums))]
    for num, freq in hash_map.items():
        li[freq - 1].append(num)

    # Step 3: collect top k from highest frequency
    res = []
    for i in range(len(li) - 1, -1, -1):
        res.extend(li[i])
        if len(res) >= k:
            return res[:k]
