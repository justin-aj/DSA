import math

best = -math.inf

score = [10, 1000, 12, 45, 140]

for i in score:
    if i > best:
        best = i

print(best)