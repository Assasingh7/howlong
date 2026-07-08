def main(n):
    for i in range(n):
        for _ in range(i+1):
            print("*", end="")
        print()
    for i in range(n-1, -1, -1):
        for _ in range(i):
            print("*", end="")
        print()

if __name__ == "__main__":
    main(5)