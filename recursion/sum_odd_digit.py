def main(n):
    if n == 0:
        return 0
    s = 0
    num = n%10
    if num%2==1:
        s+=num
    s+=main(n//10)
    return s

if __name__ == "__main__":
    print(main(123))
