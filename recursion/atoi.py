def is_num(ch):
    return '0' <= ch <= '9'
INT_MAX = 2**31-1
INT_MIN = -2**31
def helper(s, n, curr_index, sign):
    if curr_index>=len(s) or not is_num(s[curr_index]):
        return n*sign
    n= n*10+ int(s[curr_index])
    if sign*n<INT_MIN:
        return INT_MIN
    if sign*n>INT_MAX:
        return INT_MAX
    return helper(s, n, curr_index+1, sign)

def main(s):
    i = 0
    while i<len(s) and s[i] == ' ':
        i+=1
    sign =1
    if i<len(s) and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i+=1
    return helper(s, 0, i, sign)

    
if __name__ == "__main__":
    s = " -12345"
    print(main(s))