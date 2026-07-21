def is_valid(s):
    balance = 0
    for ch in s:
        if ch == '(':
            balance+=1
        else:
            balance-=1
        if balance<0:
            return False
    return balance == 0

def generate_parenthesis(s, n, res):
    if len(s) == 2*n:
        if is_valid(s):
            res.append(s)
        return res
    generate_parenthesis(s+'(', n, res)
    generate_parenthesis(s+')', n, res)
    return res
def generate_parenthesiss(s, open, close,  n, res):
    if len(s) == 2*n: 
        res.append(s)
        return res
    if open<n:
        generate_parenthesiss(s+'(',open+1, close,  n, res)
    if close<open:
        generate_parenthesiss(s+')', open, close+1, n, res)
    return res
def main():
    n = 2
    temp = []
    result = generate_parenthesiss("",0, 0, n, temp)
    for s in result:
        print(s)
main()