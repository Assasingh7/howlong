def main(n, m):
    if n == 0:
        return 1
    return n * main(n-1, m)

if __name__ == "__main__":
    sum = main(5, 5)
    print(sum)