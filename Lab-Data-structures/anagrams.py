# Your driver code (including input / output handling) should go here
from find_anagrams import find_anagrams


def main(input_file):
    """Input: input_file(a list of words)
    Output: output_file(grouped words in anagram sets)
    """
    try:
        with open(input_file, 'r') as file:  # with, 'r' mode
            words = [line.strip() for line in file]  # inspect line by line
    except FileNotFoundError:
        print("Error: Cannot read input file")
        return

    try:
        anagram_sets = find_anagrams(words)  # use find_anagrams()
    except ValueError:
        print("Invalid input")
        return

    try:
        with open('anagram_sets.txt', 'w') as output_file:  # with, 'w' mode
            for anagram_list in anagram_sets.values():
                output_file.write(f"{anagram_list}\n")
    except IOError:
        print("Error: Cannot write to the file anagram_sets.txt")
