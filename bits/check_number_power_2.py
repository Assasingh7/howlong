def main(n):
    return n>0 and  (n & (n-1)) == 0
print(main(16))