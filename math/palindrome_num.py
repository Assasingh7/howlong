def palindrome_num(n):
    num = n
    rev_num = 0
    while(num!=0):
        rev_num = 10*rev_num + num % 10
        num//=10
    return n == rev_num
if __name__ == "__main__":
    is_palindrome = palindrome_num(1221)
    print(is_palindrome)
