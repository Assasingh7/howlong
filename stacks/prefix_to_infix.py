def main(exp):
    st = []
    for ch in reversed(exp):
        if ch.isalnum():
            st.append(ch)
        else:
            op1 = st.pop() 
            op2 = st.pop() 
            st.append('('+op1+ch+op2+')')
    return st[-1]