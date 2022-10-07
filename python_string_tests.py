import string  # used to get a string of punctuation characters

s = "abcdefghijklmnopqrstuvwxyz"
print("length")
print(len(s))
print("ith (plus one) character")
print(s[2])

try:
    s[1] = "5"
except TypeError:
    print("strings are immutable")

print("slice")
# string[start:end:step]
print(s[::2])
print(s[::-2])

print("notice that an index too high on the 'end' argument doesn't error out")
print(s[:100])
print(s[25:100])

print("concatenation")
print(s[:3] + s[:4])

print("find")
print(s.find("efg"))
print(s.find("efg", 2, 10))

if "efg" in s:
    print("using 'sub_string in string' pattern is an alternative to find()")

print("use find with a starting and ending index")
print("all the same")
print(s.find("efg", 10, -1))
print(s.find("efg", 10, 100))
print(s.find("efg", 10, 25))

print("all the same")
print(s.find("efg", 3, -1))
print(s.find("efg", 3, 100))
print(s.find("efg", 3, 25))

print("return string from original after finding starting index")
target_str = "efg"
starting_idx = s.find("efg")
sub_s = s[starting_idx:starting_idx+len(target_str)]
print(sub_s)

print("If you can't find the substring find() returns -1")
print(s.find("az"))

print("starts with")
print(s.startswith("abc"))
print(s.startswith("def", 3, 100))
print(s.startswith("def", 3))
print("ends with")
print(s.endswith("xyz"))
print(s.endswith("xyz", 20))
print(s.endswith("xyz", 20, 100))

if s == "abcdefghijklmnopqrstuvwxyz":
    print("string match")

a = "hi"
b = "hi"

if a == b:
    print("string match")

print("int to string, sting to int")
s_num = "42"
print(str(42) == "42")
print(int(s_num) == 42)

print("string char to ascii/unicode/utf-8, etc value; and inverse")
print(ord("a"))
print(ord("b"))
print(ord("B"))
print(ord("4"))
print(ord(" "))
print(chr(42))
print(chr(98))
print(chr(52))
print("*", chr(31), "*")

for i in range(100):
    print(i, "->", chr(i))

print("check if string is entirely lower, upper, alpha, numeric")
print(s.isupper())
print(s.islower())
print(s.isalpha())
print(s.isnumeric())
print(s.isnumeric())

s_punc = "?"

if s_punc in string.punctuation:
    print("the single character string is a character in punctuation string")

print(string.punctuation)
print(type(string.punctuation))

print("make string lower and upper")
print(s.upper())
print(s.lower())

print("partition string into before, sep_parameter, after tuple")
print(s.partition("efg"))

print("choose a string separator for joining a list of characters")
list_s = ["a", "b", "z"]
print("".join(list_s))
print("-".join(list_s))
print(",".join(list_s))
print("abz".join(list_s))

print(bin(32))
print(type(bin(32)))
print(bin(32)[2:])
print(bin(8)[2:].zfill(6))

test_str = ""
test_str2 = "a"

if test_str2:
    print(test_str2)
else:
    print("did something go wrong?")

if test_str:
    print(test_str)
else:
    print("no string")









