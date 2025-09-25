class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        if self.head is None:
            print("")
            return
            
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        separator = " -> "
        print(separator.join(elements))
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert(self, data, i):
        if i < 0:
            raise IndexError("Index cannot be negative")
        
        new_node = Node(data)
        
        if i == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        position = 0
        
        while current and position < i - 1:
            current = current.next
            position += 1
        
        if current is None:
            raise IndexError("Index out of range")
        
        new_node.next = current.next
        current.next = new_node
    
    def delete(self, i):
        if self.head is None:
            return "None" 
        
        if i < 0:
            raise IndexError("Index cannot be negative")
        
        if i == 0:
            deleted_data = self.head.data
            self.head = self.head.next
            return deleted_data
        
        current = self.head
        position = 0
        
        while current and position < i - 1:
            current = current.next
            position += 1
        
        if current is None or current.next is None:
            return "None"  # Return string "None" for out of range index
        
        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data
    
    def index(self, data):
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def swap(self, i, j):
        # If indices are the same, no swap needed
        if i == j:
            return
        
        # Find nodes at positions i and j
        node_i_prev = None
        node_i = self.head
        index_i = 0
        while node_i and index_i < i:
            node_i_prev = node_i
            node_i = node_i.next
            index_i += 1
        
        node_j_prev = None
        node_j = self.head
        index_j = 0
        while node_j and index_j < j:
            node_j_prev = node_j
            node_j = node_j.next
            index_j += 1
        
        # If either node is not found, return without changes
        if not node_i or not node_j:
            return
        
        # Swap the nodes by updating their previous nodes' next pointers
        if node_i_prev:
            node_i_prev.next = node_j
        else:
            self.head = node_j
        
        if node_j_prev:
            node_j_prev.next = node_i
        else:
            self.head = node_i
        
        # Swap the next pointers of the nodes
        temp = node_i.next
        node_i.next = node_j.next
        node_j.next = temp

if __name__ == "__main__":
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()
    print(L.index(7))   
    print(L.index(9))   
    L.swap(1, 4)
    L.print()
    L.swap(2, 0)
    L.print()