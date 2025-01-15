from crowded_cows import crowded_cows

"""Unit tests"""


def test_crowded_cows():  # test w given examples
    assert crowded_cows([7, 3, 4, 2, 3, 4], 3) == 4
    assert crowded_cows([7, 3, 4, 2, 3, 10, 4], 3) == 3
    assert crowded_cows([7, 3, 1, 0, 4, 2, 16, 28, 3, 4], 3) == -1


def test_single_element():  # test single element
    cow_list = [5]
    K = 1
    expected = -1
    result = crowded_cows(cow_list, K)
    assert result == expected


def test_empty_list():
    cow_list = []
    K = 2
    expected = -1
    result = crowded_cows(cow_list, K)
    assert result == expected
