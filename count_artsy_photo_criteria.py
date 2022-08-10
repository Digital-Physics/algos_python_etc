# time: O(n**3)
# space: O(n) for making the reversed list (could be optimized by doing just one pass)
def one_way(n_s: int, c_s: str, x_s: int, y_s: int) -> int:
    count = 0

    for p_idx in range(n_s):
        if c_s[p_idx] == "P":
            for a_idx in range(p_idx + x_s, p_idx + y_s + 1):
                if a_idx < n_s and c_s[a_idx] == "A":
                    for b_idx in range(a_idx + x_s, a_idx + y_s + 1):
                        if b_idx < n_s and c_s[b_idx] == "B":
                            count += 1

    return count


# a photo is artsy if both the distance between the photographer P and artist A is within X and Y
# the distance between the photographer P and background B is in range
def count_artsy_photo(n: int, c: str, x: int, y: int) -> int:
    reverse = c[::-1]
    return one_way(n, c, x, y) + one_way(n, reverse, x, y)


# time: O(n**3)
# space: O(1)
def count_artsy_photo2(n: int, c: str, x: int, y: int) -> int:
    count = 0

    for p_idx in range(n):
        if c[p_idx] == "P":
            for a_idx in range(p_idx + x, p_idx + y + 1):
                if a_idx < n and c[a_idx] == "A":
                    for b_idx in range(a_idx + x, a_idx + y + 1):
                        if b_idx < n and c[b_idx] == "B":
                            count += 1

    print("PAB count only", count)
    for b_idx in range(n):
        if c[b_idx] == "B":
            for a_idx in range(b_idx + x, b_idx + y + 1):
                if a_idx < n and c[a_idx] == "A":
                    for p_idx in range(a_idx + x, a_idx + y + 1):
                        if p_idx < n and c[p_idx] == "P":
                            count += 1

    return count


print(count_artsy_photo(5, "APABA", 1, 2))
print(count_artsy_photo(5, "APABA", 2, 3))
print(count_artsy_photo(8, ".PBAAP.B", 1, 3))

print(count_artsy_photo2(5, "APABA", 1, 2))
print(count_artsy_photo2(5, "APABA", 2, 3))
print(count_artsy_photo2(8, ".PBAAP.B", 1, 3))
