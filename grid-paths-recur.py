def grid_path(n, m):
    print("Start", n, m)
    if n == 1 or m == 1:
        return 1
    else:
        print(n, m, "before")
        a = grid_path(n-1, m)
        print(n,m, "Anything", a)  ## Important thing here is that n is not updated when it returns 1. Explained below
        b = grid_path(n, m-1)
        print(n, m, "After")
        return a + b

print(grid_path(3, 3))

"""
This behavior is due to how Python handles function calls and local variables in recursion. Let's break it down:

Key Concept: Each function call has its own scope
When you make a recursive function call like grid_path(n-1, m), the parameters n and m in that new call are completely 
separate from the original call. Here's what happens step by step:

Step-by-Step Analysis:
Initial Call:
grid_path(3, 3) is called.

Local variables: n=3, m=3.
First Recursive Call:
Inside grid_path(3, 3), you make the call grid_path(n-1, m), i.e., grid_path(2, 3).

This creates a new function call with n=2, m=3.
The original n=3, m=3 are unchanged because each function call has its own independent copy of the parameters.
Second Recursive Call:
Inside grid_path(2, 3), you make the call grid_path(1, 3).

This creates another new function call with n=1, m=3.
The n=2, m=3 from the previous call remains unaffected in its scope.
Base Case:
When grid_path(1, 3) is executed, it hits the base case if n == 1 or m == 1 and returns 1.

Returning to Previous Call:
When grid_path(1, 3) returns 1, the execution returns to the grid_path(2, 3) call.

At this point, the local variable n=2 is still 2 because it was never changed. The recursive call does not alter 
the variables of the parent function.

Why n is not updated:

The n in grid_path(1, 3) is a different variable from the n in grid_path(2, 3).
Python creates a new scope for each recursive call, so changes to n in one scope do not affect n in another.
"""