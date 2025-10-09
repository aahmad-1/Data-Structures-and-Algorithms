class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.is_mirrored = False
    
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
            # When mirrored, comparison directions are reversed
            if not self.is_mirrored:
                # Normal: smaller goes left, larger goes right
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
                    # Duplicate
                    return
            else:
                # Mirrored: smaller goes right, larger goes left
                if key < curr.key:
                    if curr.right is None:
                        curr.right = Node(key)
                        return
                    curr = curr.right
                elif key > curr.key:
                    if curr.left is None:
                        curr.left = Node(key)
                        return
                    curr = curr.left
                else:
                    # Duplicate
                    return
    
    def search(self, key: int) -> bool:
        """Searches for a key in the BST"""
        curr = self.root
        while curr:
            if key == curr.key:
                return True
            elif not self.is_mirrored:
                # Normal BST
                if key < curr.key:
                    curr = curr.left
                else:
                    curr = curr.right
            else:
                # Mirrored BST
                if key < curr.key:
                    curr = curr.right
                else:
                    curr = curr.left
        return False
    
    def remove(self, key: int):
        """Removes a key from the BST using maximum node principle"""
        parent = None
        curr = self.root
        
        # Find the node to remove and its parent
        while curr and curr.key != key:
            parent = curr
            if not self.is_mirrored:
                if key < curr.key:
                    curr = curr.left
                else:
                    curr = curr.right
            else:
                if key < curr.key:
                    curr = curr.right
                else:
                    curr = curr.left
        
        if curr is None:
            return  # Key not found
        
        # Case 1: Node has two children
        if curr.left and curr.right:
            # Find max in left subtree
            # "Left subtree" means the subtree with smaller values
            # In normal BST: that's the physical left
            # In mirrored BST: that's the physical right
            max_parent = curr
            if not self.is_mirrored:
                max_node = curr.left
                while max_node.right:
                    max_parent = max_node
                    max_node = max_node.right
            else:
                max_node = curr.right
                while max_node.left:
                    max_parent = max_node
                    max_node = max_node.left
            
            # Replace curr's key with max_node's key
            curr.key = max_node.key
            
            # Remove max_node (which has at most one child on the other side)
            if not self.is_mirrored:
                child = max_node.left
                if max_parent == curr:
                    max_parent.left = child
                else:
                    max_parent.right = child
            else:
                child = max_node.right
                if max_parent == curr:
                    max_parent.right = child
                else:
                    max_parent.left = child
        
        # Case 2: Node has one or no children
        else:
            child = curr.left if curr.left else curr.right
            
            if parent is None:
                self.root = child
            elif parent.left == curr:
                parent.left = child
            else:
                parent.right = child
    
    def mirror(self):
        """Mirrors the BST by swapping left and right children of all nodes"""
        def _mirror(node):
            if node is None:
                return
            # Swap left and right children
            node.left, node.right = node.right, node.left
            # Recursively mirror subtrees
            _mirror(node.left)
            _mirror(node.right)
        
        _mirror(self.root)
        self.is_mirrored = not self.is_mirrored


if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)

    Tree.preorder()
    Tree.mirror()
    Tree.preorder()

    Tree.insert(8)
    Tree.remove(3)
    print(Tree.search(2))
    Tree.preorder()
    Tree.mirror()
    Tree.preorder()