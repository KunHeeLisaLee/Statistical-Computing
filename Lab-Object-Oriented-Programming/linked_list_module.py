class Node:
    """Class for representing a node in a linked list"""

    def __init__(self):
        self.next = None
        self.data = None

    def set_data(self, data):
        """Add data to the node

        Any previously stored data will be replaced.

        Parameters
        ----------
        data : Any
           Data to be stored in the node.
        """
        self.data = data


class LinkedList:
    """Class to create and operate on a linked list"""

    def __init__(self):
        self.head = None

    def __str__(self):
        """Method for casting the linked list as a string

        Called by str() or print().

        Returns
        -------
        str
            A string representation of the list.
        """

        if self.head is None:
            raise ValueError("List is empty")

        ret_str = ""
        current = self.head
        while current:
            ret_str = ret_str + str(current.data) + " "
            current = current.next
        return ret_str

    def insert(self, data):
        """Insert a node at the end of the linked list

        Parameters
        ----------
        data : Any
           Data to be stored in the node.
        """

        node = Node()
        node.set_data(data)
        current = self.head
        if current is None:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node

    def size(self):
        """Returns size of the linked list

        Returns
        -------
        int
            Size of the linked list.
        """

        length = 0  # starts from 0
        current = self.head
        if current is None:  # when list is empty
            length = 0
        else:  # when list is not empty
            while current:
                length += 1
                current = current.next
        return length

    def remove_duplicates(self):
        """Removes duplicate nodes from the linked list"""

        if self.head is None:
            return
        seen = set()  # create empty set
        current = self.head
        seen.add(current.data)  # add an item to a set

        while current.next:
            if current.next.data in seen:
                current.next = current.next.next  # do not add duplicate entry
            else:
                seen.add(current.next.data)  # add an item to a set
                current = current.next
