def fibo(n):
    if n<=1:
        return n
    # if n==1:
        # return 1
    return fibo(n-1) + fibo(n-2)

if __name__ == "__main__":
    n= fibo(6)
    print(n)
