from Node import Node

"""

General implementation of AVL Tree from my own Project 1 solution
-- Maggie Tieu (11/23/20)

"""

class AVLTree:
    root = None

    """ Left Rotation in case of Right-Right imbalance """
    def rotate_left(self, node):
        parent = node.right
        node.right = parent.left
        parent.left = node
        return parent

    """ Right Rotation in case of Left-Left imbalance """
    def rotate_right(self, node):
        parent = node.left
        node.left = parent.right
        parent.right = node
        return parent

    """ Left-Right Rotation in case of Left-Right imbalance """
    def rotate_left_right(self, node):
        # Left rotation on node's left child
        middle = self.rotate_left(node.left)
        node.left = middle
        # Right rotation on node
        node = self.rotate_right(node)
        return node

    """ Right-Left Rotation in case of Right-Left imbalance """
    def rotate_right_left(self, node):
        # Right rotation on node's right child
        middle = self.rotate_right(node.right)
        node.right = middle
        # Left rotation on node
        node = self.rotate_left(node)
        return node

    """ Helper function: Finds height of a node """
    def find_height(self, node):
        if node is None:
            return 0
        return node.height

    """ Helper function: Finds balance factor of a node """
    def get_balance_factor(self, node):
        return self.find_height(node.left) - self.find_height(node.right)

    """ Helper function: Insertion into tree """
    def insert_date(self, new_node, node):
        # Base case: If we reach a child of a leaf, then insert here
        # Recursive case: Traverse thru tree to find appropriate insertion point
        if node is None:
            node = new_node
            return node

        elif new_node.date > node.date:
            node.right = self.insert_date(new_node, node.right)
            # Perform any necessary rotation
            if abs(self.get_balance_factor(node)) == 2:
                if new_node.date > node.right.date:
                    node = self.rotate_left(node)
                else:
                    node = self.rotate_right_left(node)

        elif new_node.date < node.date:
            node.left = self.insert_date(new_node, node.left)
            # Perform any necessary rotation
            if abs(self.get_balance_factor(node)) == 2:
                if new_node.date < node.left.date:
                    node = self.rotate_right(node)
                else:
                    node = self.rotate_left_right(node)

        # Increment height of each node in the traversal
        node.height = 1 + max(self.find_height(node.left), self.find_height(node.right))
        return node

    """ Insert a date into tree"""
    def insert(self, date, stock_value):
        new_node = Node(int(date), int(stock_value))
        self.root = self.insert_date(new_node, self.root)

    """ Search a date in tree. Returns stock value """
    def search(self, date):
        node = self.root

        while node is not None:
            if node.date is int(date):
                return node.stock_value
            elif node.date < int(date):
                node = node.right
            elif node.date > int(date):
                node = node.left

        return None

    def print_inorder(self, node):
        if node is None:
            return

        self.print_inorder(node.left)
        print(node.date)
        print(node.stock_value)
        self.print_inorder(node.right)
