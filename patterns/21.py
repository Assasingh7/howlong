def main(n):
    for i in range(n):
        for j in range(n):
            # if i == 0 | j == 0 | j == n-1 | i == n-1:
            if i in (0, n-1) or j in (0, n-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

if __name__ == "__main__":
    main(5)