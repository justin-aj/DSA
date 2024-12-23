class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_map = set()
        i = 0
        for j in range(len(s)):
            print(s)
            print(i, j, "end")
            while s[j] in set_map:
                set_map.remove(s[i])
                i += 1
            set_map.add(s[j])
            print(j - i + 1)
        print(set_map)