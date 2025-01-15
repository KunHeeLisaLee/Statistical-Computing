from linked_list_module import LinkedList

# Instantiate an empty list
linked_list = LinkedList()

# Insert numbers into the list
linked_list.insert(11)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(11)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(5)

# Print the list
print("The linked list is:")
print(linked_list)

print("An alternative way of printing the list: " + str(linked_list))

# Instantiate an empty list
linked_list2 = LinkedList()

# Insert strings into the list
linked_list2.insert("This")
linked_list2.insert("is")
linked_list2.insert("an")
linked_list2.insert("example")
linked_list2.insert("sentence.")

# Print the list
print("The linked list is:")
print(linked_list2)
