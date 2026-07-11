def gcd(n, m):
    for i in range(min(n, m), 0, -1):
        if n%i == 0 and m%i == 0:
            return i
    return 1
if __name__ == "__main__":
    print(gcd(20, 15))
