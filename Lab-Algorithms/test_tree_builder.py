import pytest

from tree_builder import new_treemap, treemap_insert, treemap_search, \
    treemap_search_between


# This creates a "test fixture". This is an easy way to create data that's
# needed by your tests, and if one test changes the data in some way, the
# other tests get a clean untouched copy.
@pytest.fixture
def example_tree():
    example = new_treemap(4, "ducks")
    treemap_insert(example, 3, "walruses")
    treemap_insert(example, 3.5, "penguins")
    treemap_insert(example, 2, "seals")
    treemap_insert(example, 5, "whales")
    treemap_insert(example, 4.5, "otters")

    return example


def test_treemap_search(example_tree):
    assert treemap_search(example_tree, 4) == "ducks"
    assert treemap_search(example_tree, 2) == "seals"
    assert treemap_search(example_tree, 5) == "whales"

    with pytest.raises(KeyError):
        treemap_search(example_tree, 17)

    with pytest.raises(KeyError):
        treemap_search(None, 1)


def test_treemap_search_between(example_tree):
    assert treemap_search_between(example_tree, 2, 3) == ["seals"]
    assert treemap_search_between(example_tree, 2, 3.5) == \
        ["seals", "walruses"]
    assert treemap_search_between(example_tree, 1, 2) == []
    assert treemap_search_between(example_tree, 2, 6) == \
        ["seals", "walruses", "penguins", "ducks", "otters", "whales"]
