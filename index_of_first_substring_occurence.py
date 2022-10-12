def find_needle_in_haystack(haystack: str, needle: str) -> int:
    """returns the index of the first occurrence of a substring.
    if the substring doesn't exist it will return -1."""
    return haystack.find(needle)


def find_needle_in_haystack2(haystack: str, needle: str) -> int:
    """returns the index of the first occurrence of a substring.
    if the substring doesn't exist it will return -1."""
    try:
        return haystack.index(needle)
    except ValueError:
        return -1

# also see Knuth-Morris-Pratt algorithm
# https://github.com/Digital-Physics/algorithms/blob/main/knuth_morris_pratt.py


test_haystack = "leetcode"
test_needle = "leto"
test_needle2 = "etc"

print(find_needle_in_haystack(test_haystack, test_needle))
print(find_needle_in_haystack(test_haystack, test_needle2))

print(find_needle_in_haystack2(test_haystack, test_needle))
print(find_needle_in_haystack2(test_haystack, test_needle2))
