from AVLTree import AVLTree

def main():
    tree = AVLTree()

    for i in range(5):
        val = input("Enter date: ")
        stock = input("Enter stock value: ")
        tree.insert(val, stock)

    tree.print_inorder(tree.root)
    
    search_for = input("Search date: ")
    print(tree.search(search_for))


main()