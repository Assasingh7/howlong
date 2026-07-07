def main(n):
    for i in range(n-1, 0, -1):
        for _ in range(i):
            print("*", end="")
        print() 

if __name__ == "__main__":
    main(6)