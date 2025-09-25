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

if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(3)
    L.print()
    L.insert(10, 1)
    L.insert(15, 0)
    L.print()
    L.delete(0)
    L.print()