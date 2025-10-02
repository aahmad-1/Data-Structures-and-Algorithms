class HashLinear:
    def __init__(self, M: int):
        """Initialize hash table of size M"""
        self.M = M
        self.X = M  # X = M for linear probing
        self.table = [None] * M
        self.tombstone = "TOMBSTONE"
    
    def hash(self, data: str) -> int:
        """Calculate hash value for given string"""
        sum_val = 0
        for char in data:
            sum_val += ord(char)
        return sum_val % self.X
    
    def print(self):
        """Print the content of the hash table"""
        output = []
        for slot in self.table:
            if slot is None:
                output.append('F')
            elif slot == self.tombstone:
                output.append('T')
            else:
                output.append(slot)
        print(' '.join(output))
    
    def insert(self, data: str):
        """Insert data into hash table, ignoring duplicates"""
        # Check if data already exists
        if self._find(data) != -1:
            return
        
        # Calculate initial hash position
        index = self.hash(data)
        start_index = index
        
        # Linear probing to find empty or tombstone slot
        while True:
            if self.table[index] is None or self.table[index] == self.tombstone:
                self.table[index] = data
                return
            
            # Move to next slot (linear probing)
            index = (index + 1) % self.M
            
            # If we've checked all slots, table is full
            if index == start_index:
                return
    
    def delete(self, data: str):
        """Remove data from hash table"""
        index = self._find(data)
        if index != -1:
            self.table[index] = self.tombstone
    
    def _find(self, data: str) -> int:
        """Find the index of data in the table, return -1 if not found"""
        index = self.hash(data)
        start_index = index
        
        while True:
            if self.table[index] == data:
                return index
            if self.table[index] is None:
                return -1
            
            # Move to next slot
            index = (index + 1) % self.M
            
            # If we've checked all slots
            if index == start_index:
                return -1


if __name__ == "__main__":
    table = HashLinear(8)
    table.print()
    table.insert("apple")
    table.insert("orange")
    table.insert("banana")
    table.insert("grapes")
    table.insert("mango")
    table.insert("peach")
    table.insert("apple")
    table.print()
    table.delete("banana")
    table.delete("kiwi")
    table.delete("peach")
    table.print()