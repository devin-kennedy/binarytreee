class BinarySearchTree:

    # This is a Node class that is internal to the BinarySearchTree class.
    class __Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        def getVal(self):
            return self.val

        def setVal(self, newVal):
            self.val = newVal

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def setLeft(self, newLeft):
            self.left = newLeft

        def setRight(self, newRight):
            self.right = newRight

        # This method should iterate over the left side of the tree, then
        # return the val, then iterate over the right side of the tree.
        def __iter__(self):
            if self.getLeft() is not None:
                for i in self.getLeft():
                    yield i
            yield self.val

            if self.getRight() is not None:
                for i in self.getRight():
                    yield i

    def __init__(self):
        self.root = None

    # Insert something into the tree.
    def insert(self, val):
        # The __insert function is recursive and is not passed a self
        # parameter. It is static function (not a method of the class) but
        # is hidden inside so users of the class will not know it exists.
        def __insert(root, val):
            if root is None:
                return self.__Node(val)
            else:
                if val <= root.getVal():
                    return self.__Node(root.getVal(), __insert(root.getLeft(), val), root.getRight())
                else:
                    return self.__Node(root.getVal(), root.getLeft(), __insert(root.getRight(), val))

        self.root = __insert(self.root, val)

    def __iter__(self):
        if self.root is not None:
            return self.root.__iter__()
        else:
            return [].__iter__()


def main():
    s = input("Enter a list of numbers, seperated by spaces: ")
    lst = s.split()

    tree = BinarySearchTree()
    for x in lst:
        tree.insert(float(x))

    for x in tree:
        print(x)


if __name__ == "__main__":
    main()
