class Node:
    def __init__(self, key: int):
        self.key = key
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
    
    def preorder(self):  #visit node, traverse left, traverse right
        self._preorderHelp(self.root)
        print() 

    def _preorderHelp(self, node):
        if node is None:  # Base case: if node doesn't exist, return
            return
        print(node.key, end=' ')   
        self._preorderHelp(node.left)   
        self._preorderHelp(node.right)

    def inorder(self): #traverse left, visit node, traverse right
        self._inorderHelp(self.root) 
        print()

    def _inorderHelp(self, node):
        if node is None:
            return
        self._inorderHelp(node.left)
        print(node.key, end=' ')
        self._inorderHelp(node.right)
        
    def postorder(self): #traverse left,  traverse right, visit node
        self._postorderHelp(self.root)
        print()

    def _postorderHelp(self, node):
        if node is None:
            return
        self._postorderHelp(node.left)
        self._postorderHelp(node.right)
        print(node.key, end=' ')

    def breadthfirst(self):
        if self.root is None:
            print()
            return
        
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node.key, end=' ')

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)


    def insert(self, key: int):
        self.root = self._insertHelp(self.root, key)

    def _insertHelp(self, node, key):
        if node is None:
            node = Node(key)
        elif node.key > key: 
            node.left = self._insertHelp(node.left, key)
        elif node.key < key:
            node.right = self._insertHelp(node.right, key)
        
        return node
    
    def search(self, key: int):
        return self._searchHelp(self.root, key)

    def _searchHelp(self, node, key):
        if node is None:
            return False 
        
        if node.key == key:
            return True
        
        if node.key > key:
            return self._searchHelp(node.left, key)
        else:
            return self._searchHelp(node.right, key)
        
    def remove(self, key: int):
        self.root = self._removeHelp(self.root, key)

    def _removeHelp(self, node, key):
        if node is None:
            return None
        elif node.key > key:
            node.left = self._removeHelp(node.left, key)
        elif node.key < key:
            node.right = self._removeHelp(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.key = self._getmax(node.left)
                node.left = self._removemax(node.left)
        
        return node

    def _getmax(self, node):
        if node.right is None:
            return node.key
        else:
            return self._getmax(node.right)

    def _removemax(self, node):
        if node.right is None:
            return node.left
        node.right = self._removemax(node.right)

        return node
    
if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)
   
    Tree.postorder()
    Tree.inorder()
    Tree.breadthfirst()