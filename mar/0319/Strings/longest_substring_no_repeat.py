# Longest Substring Without Repeating Characters
# Pattern: Sliding Window + Hashmap
# Difficulty: Medium

def lengthOfLongestSubstring(s):
    hashmap = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        if s[right] in hashmap and hashmap[s[right]] >= left:
            left = hashmap[s[right]] + 1  # jump left to one past duplicate
        hashmap[s[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len
