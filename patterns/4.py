def main(n):
    for i in range(n):
        for _ in range(i+1):
            print(i+1, end="")
        print()
if __name__ == "__main__":
    main(5)