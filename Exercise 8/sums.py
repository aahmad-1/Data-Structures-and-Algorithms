def sums(items):
    total_sums = {0}
    
    for num in items:
        new_sums = set()
        for sum in total_sums:
            new_sums.add(sum + num)
        
        total_sums.update(new_sums)
    
    return len(total_sums) - 1

if __name__ == "__main__":
    print(sums([1, 2, 3]))                  
    print(sums([2, 2, 3]))                  
    print(sums([1, 3, 5, 1, 3, 5]))         
    print(sums([1, 15, 5, 23, 100, 55, 2])) 