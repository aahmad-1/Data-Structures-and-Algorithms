def pairs(s):
    total = 0
    count = 0  # number of '1's seen so far
    sum_positions = 0  # sum of positions of all '1's seen so far
    
    for i in range(len(s)):
        if s[i] == '1':
            # This '1' at position i contributes:
            # (i * count) - sum_positions
            # which is the sum of distances from position i to all previous '1's
            total += i * count - sum_positions
            
            # Update for next iteration
            count += 1
            sum_positions += i
    
    return total


if __name__ == "__main__":
    print(pairs("100101"))
    print(pairs("101"))
    print(pairs("100100111001"))