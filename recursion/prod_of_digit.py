def main(n):
    if n == 0:
        return 1
    num = n%10
    prod = 1
    prod = num*prod
    prod *= main(n//10)
    return prod

if __name__ == "__main__":
    p = main(123)
    print(p)