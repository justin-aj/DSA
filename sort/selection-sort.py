a = [9001, 5, 1110, 30, 0]  # This is the list of numbers we want to sort.

## Sorting in Descending Order (Biggest to Smallest)
for j in range(0, len(a)):  # Start at the first number and go through each number in the list.
    highest = a[j]  # Assume the first number in the unsorted part is the biggest.
    index = j  # Remember where this number is in the list.
    for i in range(j, len(a) - 1):  # Look at every number after the current number.
        if highest > a[i + 1]:  # If the number we're looking at is smaller than the biggest, do nothing.
            pass
        else:  # If the number we're looking at is bigger:
            index = i + 1  # Remember where the bigger number is.
            highest = a[i + 1]  # Update the biggest number.
    if a[index] > a[j]:  # If the biggest number is not in the right place:
        a[index], a[j] = a[j], a[index]  # Swap the two numbers so the biggest is in the correct spot.

print(a)  # Print the list after sorting in descending order.

## Sorting in Ascending Order (Smallest to Biggest)
for j in range(0, len(a)):  # Start at the first number and go through each number in the list.
    lowest = a[j]  # Assume the first number in the unsorted part is the smallest.
    index = j  # Remember where this number is in the list.
    for i in range(j, len(a) - 1):  # Look at every number after the current number.
        if lowest > a[i + 1]:  # If the number we're looking at is smaller than the smallest:
            index = i + 1  # Remember where the smaller number is.
            lowest = a[i + 1]  # Update the smallest number.
        else:  # If the number we're looking at is not smaller, do nothing.
            pass
    if a[index] < a[j]:  # If the smallest number is not in the right place:
        a[index], a[j] = a[j], a[index]  # Swap the two numbers so the smallest is in the correct spot.

print(a)  # Print the list after sorting in ascending order.
