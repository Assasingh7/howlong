def precedence(op):
    if op in '+-':
        return 1
    elif op in '*/':
        return 2
    elif op in '^':
        return 3
    return 0
def main(exp):
    st = []
    ans = ''
    for e in exp:
        if e.isalnum():
            ans+=e
        elif e == '(':
            st.append('(')
        elif e== ')':
            while st[-1] != '(':
                ans+=st.pop()
            st.pop()
        else:
            while st and st[-1]!='(' and precedence(e) <= precedence(st[-1]):
                ans+=st.pop()
            st.append(e)
    while st:
        ans+=st.pop()
    return ans

            
