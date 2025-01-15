from linked_list_module import LinkedList

"""Exceptions"""


class ConvergenceError(Exception):
    pass


try:
    raise ConvergenceError("My algorithm failed to converge.")
except ConvergenceError as err:
    print(err)


"""Unit tests"""
# Instantiate an empty list
linked_list = LinkedList()


def test_insert():  # test for insert()
    linked_list.insert(11)
    linked_list.insert(3)
    linked_list.insert(6)
    linked_list.insert(3)
    linked_list.insert(11)
    linked_list.insert(6)
    linked_list.insert(5)
    linked_list.insert(7)
    linked_list.insert(5)
    assert str(linked_list) == "11 3 6 3 11 6 5 7 5 "


def test_size_empty():  # test for size() when the list is empty
    empty_linked_list = LinkedList()
    assert empty_linked_list.size() == 0


def test_size_full():  # test for size() when the list is not empty
    assert linked_list.size() == 9


def test_remove_duplicates_no_dup():
    """test for remove_duplicates
    with no duplicate values"""
    sample_list = LinkedList()
    sample_list.insert(11)
    sample_list.insert(6)
    sample_list.insert(7)
    sample_list.insert(5)
    sample_list.remove_duplicates()
    assert str(sample_list) == "11 6 7 5 "


def test_remove_duplicates_yes_dup():
    """test for remove_duplicates
    with duplicate values"""
    linked_list = LinkedList()
    linked_list.insert(11)
    linked_list.insert(3)
    linked_list.insert(6)
    linked_list.insert(3)
    linked_list.insert(11)
    linked_list.insert(6)
    linked_list.insert(5)
    linked_list.insert(7)
    linked_list.insert(5)
    linked_list.remove_duplicates()
    assert str(linked_list) == "11 3 6 5 7 "


def test_insert_strings():  # test for insert() w strings
    linked_list2 = LinkedList()
    linked_list2.insert("This")
    linked_list2.insert("is")
    linked_list2.insert("an")
    linked_list2.insert("example")
    linked_list2.insert("sentence.")
    assert str(linked_list2) == "This is an example sentence. "


def test_size_strings():  # test for size() w strings
    linked_list2 = LinkedList()
    linked_list2.insert("This")
    linked_list2.insert("is")
    linked_list2.insert("an")
    linked_list2.insert("example")
    linked_list2.insert("sentence.")
    assert linked_list2.size() == 5


def test_remove_duplicates_strings():
    """test for remove_duplicates() w strings"""
    linked_list2 = LinkedList()
    linked_list2.insert("This")
    linked_list2.insert("is")
    linked_list2.insert("an")
    linked_list2.insert("example")
    linked_list2.insert("sentence.")
    linked_list2.remove_duplicates()
    assert str(linked_list2) == "This is an example sentence. "
