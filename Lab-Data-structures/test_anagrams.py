from find_anagrams import find_anagrams

"""Unit tests"""


def test_anagrams():  # test result == expected w samples
    words = ['iceman', 'cinema', 'deposit']
    expected = {
        'aceimn': ['iceman', 'cinema'],
        'deiopst': ['deposit']
    }
    result = find_anagrams(words)
    assert result == expected


def test_empty_list():  # test when input is empty list
    result = find_anagrams([])
    assert result == {}


def test_input_non_string():  # test when input is not string
    try:
        find_anagrams(['abcd', 12345])
    except ValueError as e:
        assert str(e) == "Input must be a list of strings"
    else:
        assert False, "Expected ValueError but no exception was raised"


def test_input_non_list():  # test when input is not list
    try:
        find_anagrams('abcd')
    except ValueError as e:
        assert str(e) == "Input must be a list of strings"
    else:
        assert False, "Expected ValueError but no exception was raised"
