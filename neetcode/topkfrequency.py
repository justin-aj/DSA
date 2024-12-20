import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        b = dict(sorted(a.items(), key= lambda a: a[1], reverse=True))
        return list(b.keys())[:k]

        or

        return heapq.nlargest(k, a.keys(), key=a.get)

