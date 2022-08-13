# time complexity: O(9*log((B-A), 10))?
# space complexity:

def count_same_digit_nums(a: int, b: int) -> int:
    """count digits between a and b that only use one digit"""
    return check_next(a, a, b, 0, True)


def check_next(number: int, a: int, b: int, count: int, first: bool = False):
    first_dig = str(number)[0]
    curr_len = len(str(number))

    repeated = first_dig * curr_len
    if a <= int(repeated) <= b or first:
        if not first or (a <= int(repeated) <= b):
            count += 1

        if first_dig == "9":
            return check_next(int("1" * (curr_len + 1)), a, b, count)
        else:
            first_dig = str(int(first_dig) + 1)
            return check_next(int(first_dig * curr_len), a, b, count)
    else:
        return count


print(count_same_digit_nums(75, 300))
print(count_same_digit_nums(1, 9))
print(count_same_digit_nums(999, 999))


