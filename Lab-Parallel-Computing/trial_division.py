def trial_division(n: int) -> list[int]:
    """
    Return a list of the prime factors for a natural number.
    Code is from: https://en.wikipedia.org/wiki/Trial_division
    """
    a = []               # Prepare an empty list.
    f = 2                # The first possible factor.
    while n > 1:         # While n still has remaining factors...
        if n % f == 0:   # The remainder of n divided by f might be zero.
            a.append(f)  # If so, it divides n. Add f to the list.
            n //= f      # Divide that factor out of n.
        else:            # But if f is not a factor of n,
            f += 1       # Add one to f and try again.
    return a             # Prime factors may be repeated: 12 factors to 2,2,3.
