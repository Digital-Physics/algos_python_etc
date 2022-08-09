import time
import inspect

# decorator takes any function
def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        print("Total seconds taken to run function", func.__name__, ":", stop - start)

    return inner

# naive fibonacci
# time: O(2**n) (two calls/recursive call. well it's not a balanced tree, but you do double the calls each time, so approximate?)
# space: O(n) (n is the depth of the call stack)
# call stack (tree viz):
#                   f(4)
#        f(3)                   f(2)
#   f(2)       f(1)         f(1)      f(0)
# f(1)  f(0)
#
# stack builds up to the depth of the recursive tree
# I think 2 frames are put on the stack when the function is called/returned twice in one line
# f(4)
#
# f(3)
# f(2)
# f(4)
#
# f(2)
# f(1)
# f(2)
# f(4)
#
# f(1)
# f(0)
# f(1)
# f(2)
# f(4)
#
# f(0)
# f(1)
# f(2)
# f(4)
#
# f(1)
# f(2)
# f(4)
#
# f(2)
# f(4)
#
# f(1)
# f(0)
# f(4)
#
# f(0)
# f(4)
#
# f(4)
#
# (stack empty)


@calculate_time
def recursive_wrapper_fib_1(n):
    return fib_1(n)


def fib_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_1(n-1) + fib_1(n-2)


@calculate_time
def recursive_wrapper_fib_2(n):
    return fib_2(n)


# tail recursion (the recursive call is what is returned, and we are only returning one value)
def fib_2(n, i=2, last_two=(0, 1)):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif i < n:
        last = last_two[0] + last_two[1]
        second_to_last = last_two[1]
        return fib_2(n, i+1, last_two=(second_to_last, last))
    else:
        last = last_two[0] + last_two[1]
        return last


@calculate_time
def recursive_wrapper_fib_3(n):
    return fib_3(n)


# better tail recursion
def fib_3(n, second_to_last=0, last=1):
    if n == 0:
        return second_to_last
    if n == 1:
        return last
    return fib_3(n - 1, last, second_to_last + last)


@calculate_time
def recursive_wrapper_fib_4(n):
    return fib_4(n)


# memoize it (it's like a cache)
# should we keep the memoized cache outside as a global var and not pass it as an argument?
def fib_4(n, memo={0: 0, 1: 1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib_4(n-1) + fib_4(n-2)
        return fib_4(n, memo)


recursive_wrapper_fib_1(5)
# recursive_wrapper_fib_2(37)
# recursive_wrapper_fib_3(37)
# recursive_wrapper_fib_4(37)


# inspect frames on the call stack
print(inspect.stack())
# https://sites.cs.ucsb.edu/~pconrad/cs8/topics.beta/theStack/02/
# https://code-maven.com/slides/python/stack-trace-using-inspect
