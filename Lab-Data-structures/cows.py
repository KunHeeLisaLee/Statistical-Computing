# Your driver code should go here
from crowded_cows import crowded_cows
import sys


def main(K, input_file):
    """Input: input_file(pathname of a list of breed IDs) & K(max difference)
    Output: max_breed_id(maximum breed ID)"""
    try:
        with open(input_file, 'r') as file:  # with, 'r' mode
            cow_list = list(map(int, file.read().strip().split()))
    except FileNotFoundError:
        print("Error: Cannot read input file")
        return
    except ValueError:
        print("Error: Input file contains non-integer values")
        return

    try:
        result = crowded_cows(cow_list, K)
    except ValueError:
        print("Invalid input")
        return
    print(result)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python cows.py <K> <input_file>")
        sys.exit(1)

    try:
        K = int(sys.argv[1])
    except ValueError:
        print("Error: K must be an integer")
        sys.exit(1)

    input_file = sys.argv[2]
    main(K, input_file)
