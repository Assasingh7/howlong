def main(n):
    sum = 0
    for i in range(n):
        for _ in range(i+1):
            sum +=1 
            print(sum, end=" ")
        print()

if __name__ == "__main__":
    main(5)
