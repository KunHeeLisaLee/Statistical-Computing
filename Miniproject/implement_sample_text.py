import random
import time
import matplotlib.pyplot as plt
from mcmc_algorithm.preprocess import preprocess_text
from mcmc_algorithm.mcmc_implement import mcmc


def generate_cipher():
    """
    Generate a random substitution cipher to encrypt the text.
    Output
    return: A dictionary representing the cipher.
    """
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    cipher = random.sample(alphabet, len(alphabet))
    return dict(zip(alphabet, cipher))


def encrypt_text(plaintext, cipher):
    """
    Encrypt the plaintext using the substitution cipher.
    Input
    plaintext: The text to encrypt.
    cipher: A dictionary representing the substitution cipher.
    Output
    return: The encrypted text.
    """
    return ''.join(cipher.get(c, c) for c in plaintext)


def test_diff_lengths(preprocessed_text, cipher):
    """
    Test the decryption algorithm with different encrypted text lengths.
    Input
    preprocessed_text: Preprocessed reference text
    cipher: A dictionary representing the substitution cipher.
    Output
    return: A list of tuples of (plaintext length, decrypted text).
    """
    lengths = [100, 150, 200, 250]
    results = []
    for length in lengths:
        print(f"\nTesting with plaintext length: {length}")
        plaintext = preprocessed_text[:length]
        print("Original Plaintext:", plaintext)
        encrypted_text = encrypt_text(plaintext, cipher)
        print("Encrypted Text:", encrypted_text)
        mcmc_decryptor = mcmc(preprocessed_text)
        decrypted_text = mcmc_decryptor.decryption(encrypted_text,
                                                   iterations=10000)
        print("Decrypted Text:", decrypted_text)
        results.append((length, decrypted_text))
    return results


def test_diff_p(preprocessed_text, cipher):
    """
    Test the decryption algorithm with different tuning parameters.
    Input
    preprocessed_text: Preprocessed reference text
    cipher: A dictionary representing the substitution cipher.
    Output
    return: A list of tuples containing p, accuracy, and runtime.
    """
    plaintext = preprocessed_text[:200]
    print("Original Plaintext:", plaintext)
    encrypted_text = encrypt_text(plaintext, cipher)
    print("Encrypted Text:", encrypted_text)
    tuning_par = [0.2, 0.5, 1.0, 2.0, 4.0]
    results = []
    for p in tuning_par:
        print(f"\nTesting with p = {p}")
        start_time = time.time()
        mcmc_decryptor = mcmc(preprocessed_text, p=p)
        decrypted_text = mcmc_decryptor.decryption(encrypted_text,
                                                   iterations=10000)
        end_time = time.time()
        runtime = end_time - start_time

        # Calculate accuracy
        accuracy = sum(a == b for a, b in zip(plaintext, decrypted_text)
                       ) / len(plaintext) * 100
        print("Decrypted Text:", decrypted_text)
        print(f"Decryption Accuracy: {accuracy:.2f}%")
        print(f"Runtime: {runtime:.2f} seconds")
        results.append((p, accuracy, runtime))
    return results


def test_diff_iterations(preprocessed_text, cipher, iterations):
    """
    Test the decryption algorithm with different number of iterations.
    Input
    preprocessed_text: Preprocessed reference text
    cipher: A dictionary representing the substitution cipher
    iterations: Number of iterations
    Output
    log_likelihood_scores: List of log-likelihood scores for each iteration.
    accuracy: Percentage of correctly decrypted characters.
    runtime: Total runtime of the algorithm.
    decrypted_text: Final decrypted text.
    """
    plaintext = preprocessed_text[:200]
    encrypted_text = encrypt_text(plaintext, cipher)
    mcmc_decryptor = mcmc(preprocessed_text)

    # Run the algorithm and track log of L(d)
    log_likelihood_scores = []
    current_key = mcmc_decryptor.generate_key()
    current_score = mcmc_decryptor.calculate_log_likelihood(current_key,
                                                            encrypted_text)
    start_time = time.time()
    for iteration in range(1, iterations + 1):
        proposed_key = mcmc_decryptor.propose_key(current_key)
        proposed_score = mcmc_decryptor.calculate_log_likelihood(
            proposed_key, encrypted_text)

        # Metropolis criterion
        acceptance_ratio = random.random()
        if acceptance_ratio < (proposed_score - current_score):
            current_key = proposed_key
            current_score = proposed_score

        log_likelihood_scores.append(current_score)
    end_time = time.time()
    runtime = end_time - start_time
    decrypted_text = ''.join(current_key.get(c, c) for c in encrypted_text)

    accuracy = sum(a == b for a, b in zip(plaintext, decrypted_text)
                   ) / len(plaintext) * 100
    return log_likelihood_scores, accuracy, runtime, decrypted_text


def plot_log_likelihood(preprocessed_text, cipher, iterations):
    """
    Plot log L(d) for different number of iterations.
    Input
    preprocessed_text: Preprocessed reference text
    cipher: A dictionary representing the substitution cipher
    iterations: Number of iterations
    """
    results = []
    for n_iteration in iterations:
        print(f"\nRunning MCMC for {iterations} iterations...")
        log_likelihood_scores, accuracy, runtime, decrypted_text = \
            test_diff_iterations(preprocessed_text, cipher, n_iteration)
        # Save results
        results.append((n_iteration, accuracy, runtime))

        # Plot L vs. Iteration
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, n_iteration + 1), log_likelihood_scores,
                 label=f"Iterations: {n_iteration}")
        plt.xlabel("Iteration Number")
        plt.ylabel("Log-Likelihood Score (L)")
        plt.title(f"Log-Likelihood Score vs. Iteration Number ({n_iteration})")
        plt.legend()
        plt.grid()
        plt.show()

        print(f"Decryption Accuracy: {accuracy:.2f}%")
        print(f"Runtime: {runtime:.2f} seconds")
        print(f"Decrypted Text: {decrypted_text}")


def decrypt_some_text(reference_text_path, encrypted_text_path, output_path,
                      iterations, tuning_param):
    """
    Decrypt an encrypted text file using MCMC and save the results.
    Input:
    reference_text_path: Path to the reference text file.
    encrypted_text_path: Path to the encrypted text file.
    output_path: Path to save the decrypted text.
    iterations: Number of iterations for the MCMC algorithm.
    tuning_param: Tuning parameter for MCMC.
    Output:
    decrypted_text: Decrypted text.
    """
    with open(reference_text_path, "r") as ref_file:
        reference_text = ref_file.read()
    preprocessed_reference = preprocess_text(reference_text)

    with open(encrypted_text_path, "r") as enc_file:
        encrypted_text = enc_file.read()
    preprocessed_encrypted = preprocess_text(encrypted_text)

    mcmc_decryptor = mcmc(preprocessed_reference, p=tuning_param)
    log_likelihood_scores = []
    current_key = mcmc_decryptor.generate_key()
    current_score = \
        mcmc_decryptor.calculate_log_likelihood(
            current_key, preprocessed_encrypted)

    for iteration in range(1, iterations + 1):
        proposed_key = mcmc_decryptor.propose_key(current_key)
        proposed_score = \
            mcmc_decryptor.calculate_log_likelihood(proposed_key,
                                                    preprocessed_encrypted)

        # Metropolis criterion
        acceptance_ratio = random.random()
        if acceptance_ratio < (proposed_score - current_score):
            current_key = proposed_key
            current_score = proposed_score

        log_likelihood_scores.append(current_score)

    decrypted_text = ''.join(current_key.get(c, c) for c in
                             preprocessed_encrypted)

    with open(output_path, "w") as output_file:
        output_file.write(decrypted_text)

    # Plot log-likelihood scores
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, iterations + 1), log_likelihood_scores,
             label=f"Tuning Parameter: {tuning_param}")
    plt.xlabel("Iteration Number")
    plt.ylabel("Log-Likelihood Score (L)")
    plt.title(f"Log-Likelihood Score vs. Iteration Number ({iterations})")
    plt.legend()
    plt.grid()
    plt.show()

    return decrypted_text


if __name__ == "__main__":
    reference_text_path = "reference_text.txt"
    encrypted_text_path = "some_text_encrypted.txt"
    output_path = "some_text_decrypted.txt"

    iterations = 3000
    tuning_param = 1.0

    decrypted_text = decrypt_some_text(reference_text_path,
                                       encrypted_text_path, output_path,
                                       iterations, tuning_param)

    print("\nDecrypted Text:")
    print(decrypted_text)
