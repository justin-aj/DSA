from collections import Counter

# Time Complexity: O(n)

x = Counter("geeksforgeeks")

print(x)

for i in x.elements(): # Basically returns everything in order of Count
    print(i)

counter1 = Counter(a=3, b=2)
counter2 = Counter(a=1, b=2, c=3)
print(list(counter1.elements()), list(counter2.elements()))
# Aggregate the vals from 2 lists

combined = counter1 + counter2
print(combined)  # Output: Counter({'a': 4, 'b': 4, 'c': 3})

# Even difference

difference = counter2 - counter1
print(difference, "df")  # Output: Counter({'a': 2})

# Update the existing counter

counter1.update(counter2)  # Updates counter1 in-place
print(counter1)
# Output: Counter({'a': 4, 'b': 4, 'c': 3})

from collections import Counter

# Create a Counter from a list of elements
nums = ['a', 'b', 'a', 'c', 'b', 'a']
count = Counter(nums)

# Accessing counts of specific elements
print(count.get('a'))  # Output: 3 (since 'a' appears 3 times)
print(count.get('b'))  # Output: 2 (since 'b' appears 2 times)
print(count.get('c'))  # Output: 1 (since 'c' appears 1 time)
print(count.get('d'))  # Output: None (since 'd' is not in the counter)
print(count.get('d', 0))  # Output: 0 (returns default value 0 if 'd' is not in the counter)
print(count.get)
