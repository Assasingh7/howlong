def main(n):
    if n==0:
        return 0
    
    num = n%10
    count = 0
    if num == 0:
        count+=1
    count += main(n//10)
    return count
if __name__=="__main__":
    n = 1200
    if n == 0:
        print(0)
    else:
        print(main(n))
