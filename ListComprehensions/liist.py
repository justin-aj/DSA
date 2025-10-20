from collections import Counter

import numpy as np

sq = [(i*i) for i in range(1, 10)]

print(sq)

eve = [i for i in sq if i%2 == 0]

print(eve)

for i in eve:
    if i < 0:
        print("Negative")
    elif i > 0:
        print("Positive")
    else:
        print("Zero")

for i in sq:
    if i > 100:
        print("High")
    else:
        print("Normal")


vo = ['a', 'e', 'i', 'o', 'u']
vow = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u']

count = 0

for i in vow:
    if i in vo:
        count += 1

print(count)

dict1 = {'a': 1, 'b': 2, 'f': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}

merged_dict = {**dict1, **dict2}
print(merged_dict)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

print(set1.intersection(set2))

with open("test.txt", "r", encoding='utf-8') as file:
    data = file.readlines()

print(Counter(data))

data.append("c")

with open("test.txt", "a", encoding='utf-8') as file:
    file.write("\nc")

result = ["negative" if i < 0 else "positive" if i > 0 else "zero" for i in eve]

print(result)

result = ["High" if i > 100 else "Normal" for i in sq]

print(result)

vowels = {'a', 'e', 'i', 'o', 'u'}
vow = sum([1 if i in vowels else 0 for i in vow])
print(vow)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5, 'e': 6}

for i in dict1.keys():
    if i in dict2.keys():
        dict2[i] += dict1[i]
    else:
        dict2[i] = dict1[i]

print(dict2)

dict1 = {'apple': 2, 'banana': 5, 'cherry': 1}
dict2 = {'date': 3, 'elderberry': 7, 'fig': 4}

for i in dict1.keys():
    if i in dict2.keys() and dict2[i] > 3:
        dict2[i] += dict1[i]
    else:
        dict2[i] = dict1[i] * 2

print(dict2)

dict1 = {'x': 10, 'y': 20, 'z': 30}
dict2 = {'w': 20, 'v': 40, 'u': 50}

for i in dict1.keys():
    if i in dict2.keys():
        dict2[i] += dict1[i]
    else:
        dict2[i] = dict1[i]


print(dict2.items())