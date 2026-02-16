stack = [1, 2, 3]

print(stack)

print(stack.pop()) # pop removes the element
print(stack.remove(1))
print(stack.count(4), "count")
print(stack.clear(), "clear")

stack.append(1)
stack.append(2)
stack.append(3)

#c = stack.copy()
#print(c, "copy")
print(stack.extend([2, 3]), "extend")
print(stack.insert(0, 0), "insert")
print(stack.reverse(), "reverse")
print(stack.sort(reverse=False), "sort")

print(stack)