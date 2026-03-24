# Group Anagrams
# Pattern: Hashmap + Tuple Key
# Difficulty: Medium

from collections import defaultdict

def groupAnagrams(words):
    hashmap = defaultdict(list)
    for word in words:
        arr = [0] * 26
        for c in word:
            arr[ord(c) - ord('a')] += 1
        hashmap[tuple(arr)].append(word)
    return list(hashmap.values())
