def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(triangle(3, 5, 4))
    print(triangle(-1, 2, 3))
    print(triangle(5, 9, 14))
    print(triangle(30, 12, 29))