from __future__ import annotations


def generate_power_set(s: set[int | float]) -> set[int | float]:
    """generate a set of all subsets"""
    empty_set = frozenset()
    power_set = set()
    power_set.add(empty_set)
    half_of_next = set()

    for num in s:
        for subset in power_set:
            new_subset = subset.union({num})
            half_of_next.add(new_subset)
        power_set = power_set.union(half_of_next)

    return power_set


print(generate_power_set([1, 2, 3]))
print(generate_power_set({8, 9}))
print(generate_power_set({8, 9, 9}))
print(generate_power_set([8, 9, 9]))
print(generate_power_set([8.5, 9, 9]))






