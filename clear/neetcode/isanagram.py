class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            print("start")
            print(ord(s[i]) - ord('a'))
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
            print(count)

        print(count)

        for val in count:
            if val != 0:
                return False
        return True