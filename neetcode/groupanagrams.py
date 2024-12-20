from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            j = list(i)
            j.sort()
            j = "".join(j)
            print(j, d)
            d[j].append(i)

        return list(d.values())

c = Solution()

print(c.groupAnagrams([""]))

