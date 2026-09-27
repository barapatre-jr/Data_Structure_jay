# =========================================
# FILE SYSTEM SIMULATOR USING TREE
# BINARY SEARCH TREE IMPLEMENTATION
# =========================================

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class FileSystem:

    # Insert node (BST logic)
    def insert(self, root, name):
        if root is None:
            return Node(name)

        if name < root.name:
            root.left = self.insert(root.left, name)
        else:
            root.right = self.insert(root.right, name)

        return root

    # Search node
    def search(self, root, name):
        if root is None:
            return False

        if root.name == name:
            return True
        elif name < root.name:
            return self.search(root.left, name)
        else:
            return self.search(root.right, name)

    # Inorder traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.name, end=" ")
            self.inorder(root.right)

    # Preorder traversal
    def preorder(self, root):
        if root:
            print(root.name, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.name, end=" ")


# =========================================
# MAIN PROGRAM
# =========================================

fs = FileSystem()
root = None

while True:
    print("\n========== FILE SYSTEM MENU ==========")
    print("1. Insert File/Folder")
    print("2. Search File/Folder")
    print("3. Inorder Display")
    print("4. Preorder Display")
    print("5. Postorder Display")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter file/folder name: ")
        root = fs.insert(root, name)
        print("Inserted successfully")

    elif choice == "2":
        name = input("Enter name to search: ")

        if fs.search(root, name):
            print("Found in system")
        else:
            print("Not found")

    elif choice == "3":
        print("Inorder (Sorted View):")
        fs.inorder(root)
        print()

    elif choice == "4":
        print("Preorder (Structure View):")
        fs.preorder(root)
        print()

    elif choice == "5":
        print("Postorder Display:")
        fs.postorder(root)
        print()

    elif choice == "6":
        print("Exiting system...")
        break

    else:
        print("Invalid choice")