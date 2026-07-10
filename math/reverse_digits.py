def reverse_digits(n):
    rev_num = 0
    while(n>0):
         rev_num = rev_num*10 + n%10
         n//=10
    
    return rev_num

if __name__ == "__main__":
     reversed_number = reverse_digits(123)
     print(reversed_number)