def subsets(n: int) -> list:
    total_possible_subsets = 2**n
    subset_list = []
    
    for i in range(1, total_possible_subsets):
        subset = []
        num = i
        for j in range(n):
            if num % 2 == 1:
                subset.append(j + 1)
            num = num // 2
        subset_list.append(subset)
    return subset_list

if __name__ == "__main__":
    print(subsets(1))
    print(subsets(2)) 
    print(subsets(3)) 
    print(subsets(4)) 

    S = subsets(10)
    print(S[95])
    print(S[254])
    print(S[826])