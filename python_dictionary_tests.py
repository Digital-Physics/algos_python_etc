print("dictionaries can have keys based on multiple inputs")
test_dictionary = {(1, True, "a"): 42}
print(test_dictionary)

print("you can access dictionary value using a tuple or just the elements of the tuple")
print(test_dictionary[1, True, "a"])
print(test_dictionary[(1, True, "a")])

print("be careful if one of the sub-keys is a list")
key_list = ["a", "b", "c"]
test_dictionary[1, True, "a", "b", "c"] = 43
print("this would raise a syntax error:")
print("test_dictionary[1, True, *key_list]")
print("unpack your keys first")
keys = 1, True, *key_list
print(test_dictionary[keys])
