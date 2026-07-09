def main(n):
    for i in range(n-1, -1, -1):
        for _ in range(i+1):
            print(chr(65+i), end=" ")
        print()

if __name__ == "__main__":
    main(5)