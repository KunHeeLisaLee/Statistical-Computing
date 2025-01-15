# Your function implementation(s) should go here
from collections import defaultdict


def find_anagrams(words):
    """Input: a list of words
    Output: grouped words in anagram sets
    """
    if not isinstance(words, list) or not all(isinstance(word, str)
                                              for word in words):
        raise ValueError("Input must be a list of strings")

    anagram = defaultdict(list)  # create defaultdict 'anagram'
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))  # lowercase -> sort
        anagram[sorted_word].append(word)  # assign to corresponding key
    return anagram
