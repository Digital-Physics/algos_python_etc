def climb_stairs(n: int) -> int:
    """counts the number of ways to climb n stairs with step sizes 1 and 2.
    the number of ways for n is equal to the same ways for n-1 (w/ a 1-step added at the end) +
    the number of ways for n-1 that ended in a 1-step, (take that 1-step off and add a 2-step)
    note: the Fibonacci sequence pops up"""
    prev_number_of_ways = 1  # [1] is the list of all ways to traverse a staircase containing one step
    prev_ways_ending_in_1 = 1  # and it ends (and starts, but that's besides the point) on a 1-stepper

    for i in range(2, n+1):
        # temp_old_prev = prev_number_of_ways
        # prev_number_of_ways = prev_number_of_ways + prev_ways_ending_in_1
        # prev_ways_ending_in_1 = temp_old_prev
        prev_number_of_ways, prev_ways_ending_in_1 = prev_number_of_ways + prev_ways_ending_in_1, prev_number_of_ways

    return prev_number_of_ways


for i in range(10):
    print(climb_stairs(i))



