def primes(N):
    count = 0

    for number in range(2, N + 1):        
        is_prime = True                   
        for divisor in range(2, number):  
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

    return count


if __name__ == "__main__":
    print(primes(7))  
    print(primes(15))  
    print(primes(50))  