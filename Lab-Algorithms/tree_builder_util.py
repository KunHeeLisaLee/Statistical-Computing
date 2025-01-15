# You should not need to edit this file. It provides a Node class
# that stores a key, a value, and left and right children.

class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value

        self.left = left
        self.right = right

    def show(self, level=0):
        """Print out the tree in an appealing way."""

        print(" " * level, self.key, ": ", self.value, sep="")

        if self.left is not None:
            print(" " * level, "left:", sep="")
            self.left.show(level + 2)

        if self.right is not None:
            print(" " * level, "right:", sep="")
            self.right.show(level + 2)
