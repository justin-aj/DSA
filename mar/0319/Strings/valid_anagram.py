# Valid Anagram
# Pattern: Array as Hashmap
# Difficulty: Easy

def isAnagram(s, t):
    count = [0] * 26
    for c in s:
        count[ord(c) - ord('a')] += 1
    for c in t:
        count[ord(c) - ord('a')] -= 1
    return sum(count) == 0
