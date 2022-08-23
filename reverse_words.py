# time complexity: O(string_length + word_count)?
# space complexity: O(string_length)
def reverse_words(s: str) -> str:
    """reverse the words in a string, assuming one space between words coming in and going out"""
    return " ".join(reversed(s.split(" ")))


print(reverse_words("Digital Physics is coooooolll!"))