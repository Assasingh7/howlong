def main(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end="")
        print()

if __name__ == "__main__":
    main(5)
