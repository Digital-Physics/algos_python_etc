def Hamming_distance(x: int, y: int) -> int:
    """calculate the Hamming distance between two integers.
    calc the number of bit differences when ints are converted to binary"""
    diff = bin(x ^ y)[2:]  # XOR ^ works on Ints
    print(diff)
    total = 0

    for i in range(len(diff)):
        total += int(diff[i])  # +0 or +1

    return total


print(Hamming_distance(1, 4))
print(Hamming_distance(3, 1))
print(Hamming_distance(4, 7))
print(Hamming_distance(4, 8))