class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self.insert_help(self.root, key)
    
    def insert_help(self, node, key):
        # Standard BST insertion
        if node is None:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self.insert_help(node.left, key)
        elif key > node.key:
            node.right = self.insert_help(node.right, key)
        else:
            return node  # no dupe keys allowed
        
        # Update height of current node
        node.height = 1 + max(self.get_height(node.left), 
                              self.get_height(node.right))
        
        # Get balance factor
        balance = self.get_balance(node)
        
        # LL Case
        if balance < -1 and key < node.left.key:
            return self.right_rotation(node)
        
        # RR Case
        if balance > 1 and key > node.right.key:
            return self.left_rotation(node)
        
        # LR Case
        if balance < -1 and key > node.left.key:
            return self.left_right_rotation(node)
        
        # RL Case
        if balance > 1 and key < node.right.key:
            return self.right_left_rotation(node)
        
        return node
    
    def get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.right) - self.get_height(node.left)
    
    def right_rotation(self, z):
        y = z.left
        T3 = y.right
        
        # Perform rotation
        y.right = z
        z.left = T3
        
        # Update heights
        z.height = 1 + max(self.get_height(z.left), 
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), 
                           self.get_height(y.right))
        
        return y
    
    def left_rotation(self, z):
        y = z.right
        T2 = y.left
        
        # Perform rotation
        y.left = z
        z.right = T2
        
        # Update heights
        z.height = 1 + max(self.get_height(z.left), 
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), 
                           self.get_height(y.right))
        
        return y
    
    def left_right_rotation(self, z):
        z.left = self.left_rotation(z.left)
        return self.right_rotation(z)
    
    def right_left_rotation(self, z):
        z.right = self.right_rotation(z.right)
        return self.left_rotation(z)
    
    def preorder(self):
        result = []
        self.preorder_help(self.root, result)
        print(' '.join(result))
    
    def preorder_help(self, node, result):
        if node is not None:
            balance = self.get_balance(node)
            if balance < 0:
                result.append(f"{node.key}-")
            elif balance > 0:
                result.append(f"{node.key}+")
            else:
                result.append(str(node.key))
            
            self.preorder_help(node.left, result)
            self.preorder_help(node.right, result)


if __name__ == "__main__":
    Tree = AVL()
    for key in [9, 10, 11, 3, 2, 6, 4, 7, 5, 1]:
        Tree.insert(key)
    Tree.preorder()