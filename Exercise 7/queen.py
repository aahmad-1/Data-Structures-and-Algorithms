def queen(n, m):
    
    if m > n:
        return 0
    if m == 0:
        return 1
    
    cols = set()
    posDiag = set()
    negDiag = set()
    
    def backtrack(r, queens_placed):

        #base cases to see if we've placed all the queens sucessfully or run out of rows
        if queens_placed == m:
            return 1
        if r == n:
            return 0
        
        count = 0
        count += backtrack(r + 1, queens_placed)
        
        for c in range(n):
            if c in cols:
                continue
            if (r - c) in posDiag:
                continue
            if (r + c) in negDiag:
                continue
            
            #place the queen & mark position
            cols.add(c)
            posDiag.add(r - c)
            negDiag.add(r + c)
            
            count += backtrack(r + 1, queens_placed + 1)
        
            cols.remove(c)
            posDiag.remove(r - c)
            negDiag.remove(r + c)
        
        return count
    
    return backtrack(0, 0)


if __name__ == "__main__":
    print(queen(4, 4))
    print(queen(4, 2))
    print(queen(6, 4))
    print(queen(7, 2))
    print(queen(8, 8))