import pandas as pd
import sys

# Take file name as an argument using if - else -
file_name = sys.argv[1] if len(sys.argv) > 1 else 'data/data.csv'
df = pd.read_csv(file_name)


class WordCounter:
    """ This class calculates the word frequency

    This class counts the words in a prespecified column of a CSV file.

    """

    def __init__(self, file_name):
        """ This is a constructor function

        Parameters:
        file_name: the name of the CSV file
                   (including its full absolute/relative path)
        """

        # Represents a dictionary of data that will include the final counts
        self.words = {}

        self.file_name = file_name
        self.total_num_of_words = 0

    def read(self):
        """This is a read function that reads
        the file and does some post-processing

        It reads the CSV file, then extracts the desired column and calculates
        the frequency for each individual word in the CSV column

        Also, it calculates the total number of distinct words in the column
        """

        try:
            data = pd.read_csv(self.file_name, sep=',')
            for word in data["INCIDENTNEIGHBORHOOD"]:
                self.total_num_of_words = self.total_num_of_words + 1
                self.words[str(word)] = self.words.get(word, 0) + 1

        except FileNotFoundError as file_exception:
            print('The following file is unavailable: ')
            print(str(file_exception.filename))

        except Exception as e:
            print('Generic exception occured with the following details: ')
            print(str(e))

    def sort(self):
        word_freq = []
        for key, value in self.words.items():
            word_freq.append((value, key))
        word_freq.sort(reverse=True)
        self.sorted_words = word_freq

    def calculate_probability_of_most_frequent_word(self):
        print("The most frequent word in the column is "
              + self.sorted_words[0][1])
        print("and the probability for its presence is "
              + str(self.sorted_words[0][0]/self.total_num_of_words))

    def print(self):
        print(self.words)


obj = WordCounter("./data/data.csv")
obj.read()
obj.sort()
obj.calculate_probability_of_most_frequent_word()
print("All words and their frequencies: ")
obj.print()
