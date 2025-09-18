def pairs(s):
    count_ones = 0       # number of 1s seen so far
    sum_indices = 0      # sum of indices of previous 1s
    total = 0            # final answer

    i = 0
    while i < len(s):
        if s[i] == '1':
            total += count_ones * i - sum_indices
            count_ones += 1
            sum_indices += i
        i += 1

    return total


if __name__ == "__main__":
    print(pairs("100101"))      
    print(pairs("101"))         
    print(pairs("100100111001")) 