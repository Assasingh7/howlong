def main(n):
    is_prime  = [True]*(n+1)
    is_prime[0]=is_prime[1] = False
    p = 2
    while p*p<=n:
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False

        p+=1
    return is_prime
