import random
#####
#        {}
#        |
#        t
#       / \
#       r   h
#       /  / \
#       i  e  a
#       /       \
#       e       t
#       /
#       s
#
#
print("Tries can be Nested dictioaries, hash tables, key-value pairs")
print("inventor: Ed Fredkin, OG Digital Physicist")
print("Tries are helpful for representing a dictionary of possible strings/words/prefixes/suffixes")

print("Imagine if we had an english dictionary that saved all words represented as a trie")
print("Quick lookup in this tree of valid prefixes could be helpful for pruning a Boggle word search")
boggle = [[chr(random.randint(97, 122)) for _ in range(4)] for _ in range(4)]
print(boggle)

print("so if you started searching out from the upper left letter in the boggle board, say 'k'")
print("and the only two adjacent letters were 'z', 'x', 'j'")
print("since none of 'z', 'x', 'j' are in trie_dict['k'], we can stop searching out from 'k'")
print("note: 'i' is in trie_dict['k'] because there are words like 'kite' that start with 'ki'")
print("tries are helpful for looking up valid prefixes and valid words")
print("think about how an autocomplete function could use a trie to narrow down suggestions")

class TrieNode:
    def __init__(self, character):
        self.character = character
        self.children = {}
        # self.is_terminal = False
        # self.word_insert_counter = 0


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        curr_node = self.root

        for char in word:
            if char in curr_node.children:  # go down a level/update curr node
                curr_node = curr_node.children[char]
            else:  # create node, add it, then go down a level/update curr node
                new_node = TrieNode(char)
                curr_node.children[char] = new_node
                curr_node = curr_node.children[char]  # aka new_node

        # curr_node.is_terminal = True
        # curr_node.word_insert_counter += 1

    def is_prefix(self, word):
        curr_node = self.root

        for char in word:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        return True


t = Trie()
t.insert("tries")
t.insert("the")
t.insert("that")
print("is the prefix 'th' found?:", t.is_prefix("th"))
print("is the word 'the' found?:", t.is_prefix("the"))
print("is the prefix 'thy' found?:", t.is_prefix("thy"))

print("if we wanted to know if there were any words in a normal dictionary that started 'thy', we'd have to search through each key")
print("with tries, a billion dictionary words are represented in a way that makes searching quicker")
print("with each letter in the word, we are able to narrow down the search space. it runs in linear time with respect to word length")
print("so if the length of your word is shorter than the length of the dictionary, this can help")
print("the trie 'dictionary' could also be a collection phrases, not just words, that an autocomplete app wants to retrieve quickly")
print()
print("you can have lots of variations of tries that store more information at the nodes and have other methods")
print("for instance, you could uncomment parts of the code and have a word insert counter, or something that detects suffix endings")
