def climb_stairs(n: int) -> int:
    """count the number of ways to climb stairs with step sizes 1 and 2.
    the number of ways for n is equal to the same ways for n-1 (with 1 step added at the end) +
    the number of ways for n-1 that ended in a 1-step, (take that 1-step off and add a 2-step)
    note: the Fibonacci sequence pops up"""
    i = 1
    prev_number_of_ways = 1
    prev_ways_ending_in_1 = 1
    for i in range(2, n+1):
        temp_old_prev = prev_number_of_ways
        prev_number_of_ways = prev_number_of_ways + prev_ways_ending_in_1
        prev_ways_ending_in_1 = temp_old_prev

    return prev_number_of_ways


print(climb_stairs(5))



