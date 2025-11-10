def jumps(n, a, b):  #DP bottom-up approach
    
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(1, n+1):
        if i >= a:
            dp[i] += dp[i-a]
        
        if i >= b:
            dp[i] += dp[i-b]
    
    return dp[n]



if __name__ == "__main__":
    print(jumps(4, 1, 2))
    print(jumps(8, 2, 3))
    print(jumps(11, 6, 7))
    print(jumps(30, 3, 5))
    print(jumps(100, 4, 5))