def main(s):
    res = ''
    n = len(s)
    level = 0
    for ch in s:
        if ch == '(':
            if level>0:
                res+='('
            level+=1
        elif ch == ')':
            level -= 1
            if level>0:
                res+=')'
    return res

print(main("((()))"))