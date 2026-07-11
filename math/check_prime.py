#  Brute force 
def prime_checker(n):
    cnt = 0
    for i in range(2, n+1):
        if n % i == 0:
            cnt += 1
    
    return cnt == 1

# Optimal 
def prime_check(n):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1
        if n // i != i:
            cnt += 1
    return cnt == 2
if __name__ == "__main__":
    print(prime_checker(4))
    print(prime_check(5))