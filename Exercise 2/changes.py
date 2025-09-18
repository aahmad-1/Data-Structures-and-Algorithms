def changes(A):
    if len(A) <= 1:
        return 0
    
    count = 0
    i = 0
    
    while i < len(A) - 1:
        if A[i] == A[i + 1]:
            new_value = A[i] + 1 
            
            while (i + 2 < len(A) and new_value == A[i + 2]) or new_value == A[i]:
                new_value += 1
            
            A[i + 1] = new_value
            count += 1
        i += 1
    
    return count

if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # Expected: 2
    print(changes([1, 2, 3, 4, 5]))     # Expected: 0  
    print(changes([1, 1, 1, 1, 1]))     # Expected: 2