capacity = 10
items = [[1, 2], [4, 3], [5, 6], [6, 7]]

print("if-else is done up front in list comprehension syntax")
if_else_comp_list = [0 if (cap < items[0][1]) else items[0][0] for cap in range(capacity)]
print(if_else_comp_list)

print("standalone if condition is done at the end of the list comprehension syntax")
just_if = [0 for cap in range(capacity) if (cap < items[0][1])]
print(just_if)
