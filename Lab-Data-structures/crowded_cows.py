# Your implementation of crowded_cows should go here
def crowded_cows(cow_list, K):
    """Input: cow_list(a list of breed IDs) & K(max difference)
    Output: max_breed_id(maximum breed ID)"""
    if not isinstance(cow_list, list) or not all(isinstance(breed_id, int)
                                                 for breed_id in cow_list):
        raise ValueError("Input cow_list must be a list of integers")

    if not isinstance(K, int) or K < 1:
        raise ValueError("K must be an integer greater than or equal to 1")

    last = {}  # dictionary: keep track of the last seen position
    max_breed_id = -1  # default: when no crowded cows

    for i, breed_id in enumerate(cow_list):  # index + value
        if breed_id in last and i - last[breed_id] <= K:  # calculate diff
            max_breed_id = max(breed_id, max_breed_id)
        last[breed_id] = i

    return max_breed_id
