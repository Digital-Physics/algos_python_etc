# naive approach
# time: O(n) (we have n calls)
# space: O(n) (and the call stack grows)
#
# call stack over time:
# f(7) = 7*f(6) so it needs f(6) before it can return an answer
#
# f(6) = 6*f(5)
# f(7) = times(7, f(6))
#
# f(5)
# f(6)
# f(7)
#
# ...
#
# f(1)
# f(2)
# f(3)
# f(4)
# f(5)
# f(6)
# f(7)
#
# f(2)
# f(3)
# f(4)
# f(5)
# f(6)
# f(7)
#
# f(3)
# f(4)
# f(5)
# f(6)
# f(7)
#
# ...
#
# f(7) = 5040
#
# (stack empty)
def factorial_1(n):
    if n <= 1:
        return 1
    else:
        return n*factorial_1(n-1)

# Tail Recursion (The last thing it does is return a recursive call all by itself, like an equivalence)
# time: O(n) (we have n calls)
# space: O(1) (we only have to keep the most recent call on the stack)
#
# call stack:
# f(7) = f(6,7) so it only needs to return f(6,7) going forward. pop f(7), push f(6,7) to the call stack.
#
# f(6,7)
#
# f(5,42)
#
# ...
#
# f(1, 5040)
def factorial_2(n, running_product=1):
    if n <= 1:
        return running_product
    else:
        return factorial_2(n-1, running_product*n)


print(factorial_1(7))
print(factorial_2(7))

