from AVLTree import AVLTree

def main():
    tree = AVLTree()

    for i in range(20050101, 20201127):
        #val = input("Enter date: ")
        #stock = input("Enter stock value: ")
        tree.insert(i, 1)

    tree.print_inorder(tree.root)
    
    search_for = input("Search date: ")
    print(tree.search(search_for))


main()