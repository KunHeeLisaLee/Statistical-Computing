import random
import math
from collections import Counter
import string
from mcmc_algorithm.preprocess import preprocess_text
from line_profiler import profile


class mcmc:
    """
    Implements MCMC algorithm for decrypting encrypted text.
    """
    @profile
    def __init__(self, reference_text: str, p: float = 1.0):
        """
        Initialize the decryptor.
        Input
        reference_text: Preprocessed reference text
        p: Tuning parameter, starts at 1.0
        """
        try:
            if p <= 0:
                raise ValueError("Tuning parameter must be greater than 0.")
            self.reference_text = preprocess_text(reference_text)
            self.frequency = self.calculate_frequency()
            self.p = p
            self.top_key = {}
            self.top_score = float('-inf')
        except Exception as e:
            raise Exception(f"Error initializing mcmc class: {e}")

    @profile
    def calculate_frequency(self) -> dict:
        """
        Calculate the frequency of character pairs in the text.
        Input
        text: Input text
        Output
        return: Dictionary of character pair frequencies
        """
        try:
            freq = Counter()
            for i in range(len(self.reference_text) - 1):
                pair = self.reference_text[i:i+2]
                freq[pair] += 1
            return freq
        except Exception as e:
            raise Exception(f"Error calculating frequency: {e}")

    @profile
    def calculate_log_likelihood(self, decryption_key: dict,
                                 encrypted_text: str) -> float:
        """
        Calculate the log likelihood L(d) of a decryption key.
        Input
        decryption_key: current decryption key
        encrypted_text: encrypted text
        Output
        return: Log likelihood L(d)
        """
        try:
            if not isinstance(decryption_key, dict):
                raise TypeError("Decryption key must be a dictionary.")
            if not encrypted_text.strip():
                raise ValueError("Encrypted text cannot be empty.")

            decrypted_text = ''.join(decryption_key.get(c, c) for c
                                     in encrypted_text)
            log_likelihood = 0
            for i in range(1, len(decrypted_text)):
                pair = decrypted_text[i-1:i+1]
                b = max(1, self.frequency.get(pair, 0))
                log_likelihood += math.log(b)
            return log_likelihood
        except Exception as e:
            raise Exception(f"Error calculating log-likelihood: {e}")

    @profile
    def generate_key(self) -> dict:
        """
        Generate a random decryption key (permutation of the alphabet).
        Output
        return: Random decryption key
        """
        try:
            alphabet = list(string.ascii_lowercase)
            generated = random.sample(alphabet, len(alphabet))
            return dict(zip(alphabet, generated))
        except Exception as e:
            raise Exception(f"Error generating random key: {e}")

    @profile
    def propose_key(self, current_key: dict) -> dict:
        """
        Propose a new decryption key by swapping two characters.
        Input
        current_key: Current decryption key
        Output
        return: Proposed decryption key
        """
        try:
            if not isinstance(current_key, dict):
                raise TypeError("Current key must be a dictionary.")
            key = current_key.copy()
            keys_list = list(key.keys())
            a, b = random.sample(keys_list, 2)
            key[a], key[b] = key[b], key[a]
            return key
        except Exception as e:
            raise Exception(f"Error proposing new key: {e}")

    @profile
    def decryption(self, encrypted_text: str, iterations: int = 10000) -> str:
        """
        Perform MCMC decryption algorithm.
        Input
        encrypted_text: Encrypted text
        iterations: Number of iterations
        Output
        return: Decrypted text
        """
        try:
            if iterations <= 0:
                raise ValueError("Number of iterations must be greater than 0")
            encrypted_text = preprocess_text(encrypted_text)
            current_key = self.generate_key()
            current_score = self.calculate_log_likelihood(current_key,
                                                          encrypted_text)

            for _ in range(iterations):
                proposed_key = self.propose_key(current_key)
                proposed_score = self.calculate_log_likelihood(proposed_key,
                                                               encrypted_text)

                acceptance_ratio = math.exp((proposed_score -
                                             current_score) * self.p)
                if random.random() < acceptance_ratio:
                    current_key = proposed_key
                    current_score = proposed_score

                if current_score > self.top_score:
                    self.top_key = current_key
                    self.top_score = current_score

            return ''.join(self.top_key.get(c, c) for c in encrypted_text)
        except Exception as e:
            raise Exception(f"Error during decryption: {e}")
