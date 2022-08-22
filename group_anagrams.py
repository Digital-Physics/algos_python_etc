# the esoteric thing we do here of note is to hash a frozenset of dictionary items (list of (key, value) tuples)
# this was done because we wanted to quickly look up whether a distribution of letters (stored as dict) had been seen already
def group_anagrams(string_list: list[str]) -> list[list[str]]:
    """group a list of strings into sets of anagrams"""
    list_of_tuples = []  # word/string, counter/distribution of word/string represented as a dictionary

    for string in string_list:
        dist_dict = get_dictionary_distribution(string)
        # print("dist", dist_dict)
        list_of_tuples.append((string, dist_dict))

    # alternatively, we could narrow down potential dictionaries through trie-like structure as we create word distribution dictionary
    return tups_to_groups(list_of_tuples)


def get_dictionary_distribution(word: str) -> dict:
    temp_dict = {}

    for letter in word:
        if letter in temp_dict:
            temp_dict[letter] += 1
        else:
            temp_dict[letter] = 1

    return temp_dict


def tups_to_groups(list_of_dists: list[(str, dict)]) -> list[list[str]]:
    output_dict = {}

    for tup in list_of_dists:
        print(tup[1])
        print("frozen set:", frozenset(tup[1].items()))
        print("hash of frozen dictionary:", hash(frozenset(tup[1].items())))
        if hash(frozenset(tup[1].items())) in output_dict:
            output_dict[hash(frozenset(tup[1].items()))].append(tup[0])
        else:
            output_dict[hash(frozenset(tup[1].items()))] = [tup[0]]

    return list(output_dict.values())


print(group_anagrams([""]))
print(group_anagrams(["a"]))
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))



