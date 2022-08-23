def find_repeated_dna_seq(s: str) -> list[str]:
    """return sequences in DNA that are of length 10 and repeat"""
    trie = Trie()
    return trie.get_solution(s)


class TrieNode:
    def __init__(self, letter: chr, depth: int = 0) -> None:
        self.val = letter
        self.children = {}
        self.depth = depth


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode("")
        self.ending_idx = []
        self.solution = set()

    def insert(self, word: str, starting_i: int) -> None:
        curr_node = self.root

        for i, char in enumerate(word):
            if char in curr_node.children:  # go down a level/update curr node
                curr_node = curr_node.children[char]
                if curr_node.depth == 10:
                    self.ending_idx.append(starting_i + i)
            else:  # create node, add it, then go down a level/update curr node
                new_node = TrieNode(char, curr_node.depth + 1)
                curr_node.children[char] = new_node
                curr_node = curr_node.children[char]  # aka new_node

    def get_solution(self, word: str) -> list[str]:
        # can we reduce this time complexity?
        for i in range(len(word)):
            self.insert(word[i:], i)

        for r_i in self.ending_idx:
            self.solution.add(word[r_i - 9: r_i+1])

        return list(self.solution)


print(find_repeated_dna_seq("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(find_repeated_dna_seq("AAAAAAAAAAAAA"))
print(find_repeated_dna_seq("AAAAAAAAAAA"))
print(find_repeated_dna_seq("AAAAAAAAAA"))





