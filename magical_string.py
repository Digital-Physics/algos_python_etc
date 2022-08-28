def magical_string_generator(n: int) -> int:
    """count number of 1s in first n numbers of a magical string.
    the string is magical because concatenating the number of consecutive 1s and 2s
    gives the number itself"""
    # reason out the start of the string sequence starting from 1
    # initialize it so magical string is longer than str_idx reference
    magical_string = [1, 2, 2]
    one_counter = 1
    str_idx = 2

    while len(magical_string) < n:
        if magical_string[str_idx] == 1:
            next_val = 2 if magical_string[-1] == 1 else 1
            if next_val == 1:
                one_counter += 1
            magical_string.append(next_val)
            str_idx += 1
        else:
            next_val = 2 if magical_string[-1] == 1 else 1
            if next_val == 1:
                one_counter += 2
            magical_string.append(next_val)
            magical_string.append(next_val)
            str_idx += 1

    if len(magical_string) > n and magical_string[-1] == 1:
        return one_counter - 1
    else:
        return one_counter


for i in range(11):
    print(magical_string_generator(i))


