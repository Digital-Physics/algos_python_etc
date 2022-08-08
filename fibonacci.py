import time


# decorator takes any function
def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        print("Total seconds taken to run function", func.__name__, ":", stop - start)

    return inner

# naive fibonacci
# time: O(2**n) (well it's not a balanced tree, but you do double the calls each time, so approximate?)
# space: O(n) (n is the depth of the call stack)
# call stack (tree viz):
#                   f(4)
#        f(3)                   f(2)
#   f(2)       f(1)         f(1)      f(0)
# f(1)  f(0)
#
# stack builds up to the depth of the recursive tree
# f(1)
# f(2)
# f(3) first needs f(2)
# f(4) = needs f(3) and then f(2)
#
# before it goes down to
# f(2)
# f(3) first needs f(2)
# f(4) = needs f(3) and then f(2)
#
# and then back up to
#
# f(0)
# f(2) already has f(1) but still needs f(0)
# f(3) first needs f(2) then f(1)
# f(4) = needs f(3) and then f(2)
#
# f(2) has both f(1) and f(0) now so it will be popped off the stack when it returns the value next step
# f(3)
# f(4)
#
# ...
#


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


# tail recursion (each time we are returning one thing)
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


recursive_wrapper_fib_1(37)
recursive_wrapper_fib_2(37)
recursive_wrapper_fib_3(37)
recursive_wrapper_fib_4(37)



