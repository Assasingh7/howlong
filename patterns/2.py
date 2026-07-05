def main(n):
    for i in range(n):
        for _ in range(i):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    main(5)
