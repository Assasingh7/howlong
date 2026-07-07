def main(n):
    for i in range(n-1, 0, -1):
        for j in range(i):
            print(j+1, end="")
        print()
if __name__ == "__main__":
    main(6)


