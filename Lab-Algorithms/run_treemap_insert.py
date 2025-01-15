from tree_builder import new_treemap, treemap_insert

tree = new_treemap(50, "root")  # initialize treemap

treemap_insert(tree, 1, "left")
treemap_insert(tree, 8, "right")
treemap_insert(tree, 12, "left-left")
treemap_insert(tree, 20, "left-right")
treemap_insert(tree, 2, "right-left")
treemap_insert(tree, 9, "right-right")

tree.show()
