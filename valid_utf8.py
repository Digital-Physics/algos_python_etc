def valid_UTF8(l: list[int]) -> bool:
    """check valid UTF-8 bytes.
    UTF-8 is a variable-width character encoding...
    Consisting of 1-4 bytes(8-bits) w/ certain prefix properties.
    https://en.wikipedia.org/wiki/UTF-8"""
    i = 0

    while i < len(l):
        print("current byte in one binary format:", format(l[i], "b"))
        print("current byte in another format:", bin(l[i])[2:].zfill(8))
        if bin(l[i])[2:].zfill(8)[0] == "0":
            print("single byte")
            i += 1
        elif bin(l[i])[2:].zfill(8)[:3] == "110" and i + 1 < len(l):
            print("double byte")
            if bin(l[i + 1])[2:].zfill(8)[:2] == "10":
                i += 2
            else:
                return False
        elif bin(l[i])[2:].zfill(8)[:4] == "1110" and i + 2 < len(l):
            print("triple byte")
            if bin(l[i + 1])[2:].zfill(8)[:2] == "10" and bin(l[i + 2])[2:].zfill(8)[:2] == "10":
                i += 3
            else:
                return False
        elif bin(l[i])[2:].zfill(8)[:5] == "11110" and i + 3 < len(l):
            print("quadruple byte")
            if bin(l[i + 1])[2:].zfill(8)[:2] == "10" and bin(l[i + 2])[2:].zfill(8)[:2] == "10" and bin(l[i + 3])[2:].zfill(8)[:2] == "10":
                i += 4
            else:
                return False
        else:
            return False

    return True


print(valid_UTF8([197, 130, 1]))
print(valid_UTF8([235, 140, 4]))

