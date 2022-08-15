# not complete
def get_mail(v: list[int], c: int, s: float) -> float:
    """expected value of mail w/ values v, w/ cost to enter mail room c, and prob of stolen package(s) on a day s"""
    expected_total = []

    for i in range(len(v)):
        expected_total.append(sum([v[j]*(1-s)**(i-j) for j in range(i + 1)]))

    print(expected_total)


get_mail([10, 2, 8, 6, 4], 3, 0.15)
print(10*0.85**2+1.7+8)






