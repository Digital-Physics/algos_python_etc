# time complexity: O(string_length + word_count)?
# space complexity: O(string_length)
def reverse_words(s: str) -> str:
    """reverse the words in a string, assuming one space between words coming in and going out"""
    # return " ".join(reversed(s.split(" ")))
    # return " ".join(s.split(" ")[::-1])
    words = s.split(" ")
    words.reverse()  # in place needs to be done ahead of time, not in one line, i think
    return " ".join(words)


print(reverse_words("Digital Physics is coooooolll!"))

