import pytest
from mcmc_algorithm.mcmc_implement import mcmc


@pytest.fixture
def setup_mcmc():
    """
    Set up reference and encrypted text for testing.
    """
    reference_text = "this is a test reference text"
    encrypted_text = "uvwx yz uvwx yz lidfsli"  # Encrypted text
    mcmc_decryptor = mcmc(reference_text)
    return mcmc_decryptor, encrypted_text


def test_calculate_frequency(setup_mcmc):
    """
    Test the frequency calculation of character pairs.
    """
    mcmc_decryptor, _ = setup_mcmc
    freq = mcmc_decryptor.calculate_frequency()
    assert isinstance(freq, dict)
    assert len(freq) > 0


def test_generate_key(setup_mcmc):
    """
    Test the random key generation.
    """
    mcmc_decryptor, _ = setup_mcmc
    key = mcmc_decryptor.generate_key()
    assert all(c in key for c in "abcdefghijklmnopqrstuvwxyz")


def test_propose_key(setup_mcmc):
    """
    Test that proposing a new key generates a valid and different key.
    """
    mcmc_decryptor, _ = setup_mcmc
    key = mcmc_decryptor.generate_key()
    new_key = mcmc_decryptor.propose_key(key)
    assert key != new_key


def test_decryption(setup_mcmc):
    """
    Test the MCMC decryption process.
    """
    mcmc_decryptor, encrypted_text = setup_mcmc
    decrypted_text = mcmc_decryptor.decryption(encrypted_text, iterations=100)
    assert isinstance(decrypted_text, str)
