from AVLTree import AVLTree

def main():
    tree = AVLTree()

    for i in range(5):
        val = input("Enter a number: ")
        tree.insert(val)

    tree.print_inorder(tree.root)


main()