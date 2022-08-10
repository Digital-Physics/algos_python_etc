import sys
print(sys.version)
# an alternative version for Python users before 3.9
# from typing import List
# https://stackoverflow.com/questions/39458193/using-list-tuple-etc-from-typing-vs-directly-referring-type-as-list-tuple-etc

print("Type hints showing input and output data structures aren't required but can be useful")
print("they can help somebody new understand your code better")
print("they can also be used to check correctness")
print("functional programming is all about types and composing functions end to end")

r = 2
c = 3
g = [[0, 0, 1],
     [1, 0, 1]]


def get_hit_probability(rows: int, cols: int, grid: list[list[int]]) -> float:
    total = sum([sum(row) for row in grid])
    return total / (rows * cols)


print(get_hit_probability(r, c, g))




