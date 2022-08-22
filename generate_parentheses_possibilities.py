# we leverage the fact that trying to add a duplicate string to a set won't add any additional elements
def gen_parentheses(n: int, inner_paren_set: set[str] = {"()"}, step: int = 1) -> set[str]:
    """generate all legal parentheses orderings of n pairs of parenthesis"""
    if step == n:
        return inner_paren_set
    else:
        temp_set = set()

    for paren_str in inner_paren_set:
        temp_str1 = "()" + paren_str
        temp_str2 = "(" + paren_str + ")"
        temp_str3 = paren_str + "()"
        temp_set.add(temp_str1)
        temp_set.add(temp_str2)
        temp_set.add(temp_str3)
        print("temp", temp_set)

    inner_paren_set = temp_set

    return gen_parentheses(n, inner_paren_set, step + 1)


print(gen_parentheses(3))





