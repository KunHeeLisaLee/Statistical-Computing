"""Build trees.

tree_builder_util.py defines a thing called a Node. A node stores a key, a
value, and left and right children. You can access and change these with dot
notation, and the new_treemap() function below creates a Node with a key and a
value.

Example:
n = new_treemap(4, "walruses")
n.key   #=> 4
n.value #=> walruses

n2 = new_treemap(5, "ducks")
n.right = n2

n.show() # prints out the tree

A node's .left and .right are None until they are set; you can check this with
"node.left is None" and "node.right is None".

Consult test_tree_builder.py for example uses of the functions below.
"""

from tree_builder_util import Node


def new_treemap(key, value):
    """Initialize a treemap with one key and one value.

    key: one key. The key must be a Python value that can be compared
        with < and ==.
    value: a value to be stored under that key. Values can be any type.

    Returns a new treemap containing one key-value pair.
    """

    return Node(key, value)


def treemap_insert(treemap, key, value):
    """Insert one item into a treemap.

    Duplicate keys are not allowed. If the key is already in the treemap,
    the previous value is replaced with the new value.

    treemap: The treemap to insert into.
    key: The key to insert under.
    value: The value to insert.

    Returns the treemap with new item inserted.
    """

    if key == treemap.key:
        treemap.value = value  # replace with the new value
    elif key < treemap.key:
        if treemap.left is None:
            treemap.left = Node(key, value)  # insert as left child
        else:
            treemap_insert(treemap.left, key, value)
    else:
        if treemap.right is None:
            treemap.right = Node(key, value)  # insert as right child
        else:
            treemap_insert(treemap.right, key, value)

    return treemap


def treemap_search(treemap, key):
    """Find an item in a treemap, using its key, and return its value.

    treemap: The treemap to search.
    key: The key to search for.

    Returns the value corresponding to the key. Raises a KeyError if no such
    key is stored in the treemap.
    """

    if treemap is None:
        raise KeyError(key)

    if key < treemap.key:
        return treemap_search(treemap.left, key)  # search from left side
    elif key == treemap.key:
        return treemap.value
    else:
        return treemap_search(treemap.right, key)  # search from right side


def treemap_search_between(treemap, key_lo, key_hi):
    """Find all items in the treemap such that key_lo <= key < key_hi.

    treemap: The treemap to search.
    key_lo: Find keys greater than or equal to this key.
    key_hi: Find keys strictly less than this key.

    Returns a list of all values with keys in this range, in order of their
    keys. If none are found, returns the empty list.
    """

    assert key_lo < key_hi, "Key range must be a nonempty interval"

    if treemap is None:
        return []

    result = []

    if treemap.key >= key_lo:  # changed to key_lo
        result.extend(treemap_search_between(treemap.left, key_lo, key_hi))

    if key_lo <= treemap.key < key_hi:
        result.append(treemap.value)

    if treemap.key < key_hi:  # changed to key_hi
        result.extend(treemap_search_between(treemap.right, key_lo, key_hi))

    return result
