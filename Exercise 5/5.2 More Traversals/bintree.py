class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    def preorder(self):
        """Prints BST in preorder traversal"""
        def _preorder(node):
            if node:
                print(node.key, end=' ')
                _preorder(node.left)
                _preorder(node.right)
        
        _preorder(self.root)
        print()
    
    def postorder(self):
        """Prints BST in postorder traversal"""
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                print(node.key, end=' ')
        
        _postorder(self.root)
        print()
    
    def inorder(self):
        """Prints BST in inorder traversal"""
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.key, end=' ')
                _inorder(node.right)
        
        _inorder(self.root)
        print()
    
    def breadthfirst(self):
        """Prints BST in breadth-first (level-order) traversal"""
        if self.root is None:
            print()
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.key, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()
    
    def insert(self, key: int):
        """Inserts a key into the BST, ignoring duplicates"""
        if self.root is None:
            self.root = Node(key)
            return
        
        curr = self.root
        while True:
            if key < curr.key:
                if curr.left is None:
                    curr.left = Node(key)
                    return
                curr = curr.left
            elif key > curr.key:
                if curr.right is None:
                    curr.right = Node(key)
                    return
                curr = curr.right
            else:
                # Duplicate key, ignore
                return
    
    def search(self, key: int) -> bool:
        """Searches for a key in the BST"""
        curr = self.root
        while curr:
            if key == curr.key:
                return True
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return False
    
    def remove(self, key: int):
        """Removes a key from the BST using maximum node principle"""
        def _find_max(node):
            while node.right:
                node = node.right
            return node
        
        parent = None
        curr = self.root
        
        # Find the node to remove and its parent
        while curr and curr.key != key:
            parent = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        
        if curr is None:
            return  # Key not found
        
        # Case 1: Node has two children
        if curr.left and curr.right:
            # Find max in left subtree
            max_parent = curr
            max_node = curr.left
            while max_node.right:
                max_parent = max_node
                max_node = max_node.right
            
            # Replace curr's key with max_node's key
            curr.key = max_node.key
            
            # Now remove max_node (which has at most left child)
            if max_parent == curr:
                max_parent.left = max_node.left
            else:
                max_parent.right = max_node.left
        
        # Case 2: Node has one or no children
        else:
            child = curr.left if curr.left else curr.right
            
            if parent is None:
                self.root = child
            elif parent.left == curr:
                parent.left = child
            else:
                parent.right = child


if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)
   
    Tree.postorder()
    Tree.inorder()
    Tree.breadthfirst()