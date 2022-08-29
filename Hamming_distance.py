def Hamming_distance(x: int, y: int) -> int:
    """calculate the Hamming distance = bit-wise difference between two binary numbers"""
    diff = bin(x ^ y)[2:]
    print(diff)
    total = 0

    for i in range(len(diff)):
        total += int(diff[i])  # +0 or +1

    return total


print(Hamming_distance(1, 4))
print(Hamming_distance(3, 1))
print(Hamming_distance(4, 7))
print(Hamming_distance(4, 8))