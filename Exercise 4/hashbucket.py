class HashBucket:
    def __init__(self, M: int, B: int):
        """Initialize hash table of size M with B buckets"""
        self.M = M
        self.B = B
        self.X = B  # X = B for bucket hashing
        self.bucket_size = M // B
        self.table = [None] * M
        self.overflow = []
        self.tombstone = "TOMBSTONE"
    
    def hash(self, data: str) -> int:
        """Calculate hash value (bucket number) for given string"""
        sum_val = 0
        for char in data:
            sum_val += ord(char)
        return sum_val % self.X
    
    def print(self):
        """Print the content of the hash table and overflow array"""
        output = []
        for slot in self.table:
            if slot is None:
                output.append('F')
            elif slot == self.tombstone:
                output.append('T')
            else:
                output.append(slot)
        
        # Add overflow items (skip tombstones in overflow)
        for item in self.overflow:
            if item != self.tombstone:
                output.append(item)
        
        print(' '.join(output))
    
    def insert(self, data: str):
        """Insert data into hash table, ignoring duplicates"""
        # Check if data already exists
        if self._find(data)[0] != -1:
            return
        
        # Calculate bucket number
        bucket_num = self.hash(data)
        bucket_start = bucket_num * self.bucket_size
        bucket_end = bucket_start + self.bucket_size
        
        # Try to insert in the assigned bucket using linear probing
        for i in range(bucket_start, bucket_end):
            if self.table[i] is None or self.table[i] == self.tombstone:
                self.table[i] = data
                return
        
        # If bucket is full, add to overflow
        self.overflow.append(data)
    
    def delete(self, data: str):
        """Remove data from hash table"""
        index, is_overflow = self._find(data)
        if index != -1:
            if is_overflow:
                self.overflow[index] = self.tombstone
            else:
                self.table[index] = self.tombstone
    
    def _find(self, data: str):
        """Find the index of data, return (index, is_overflow) or (-1, False) if not found"""
        # Calculate bucket number
        bucket_num = self.hash(data)
        bucket_start = bucket_num * self.bucket_size
        bucket_end = bucket_start + self.bucket_size
        
        # Search in the assigned bucket
        for i in range(bucket_start, bucket_end):
            if self.table[i] == data:
                return (i, False)
        
        # Search in overflow
        for i, item in enumerate(self.overflow):
            if item == data:
                return (i, True)
        
        return (-1, False)


if __name__ == "__main__":
    table = HashBucket(8, 4)
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