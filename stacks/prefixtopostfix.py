def main(exp):
    st = []
    for ch in reversed(exp):
        if ch.isalnum():
            st.append(ch)
        else:
            op1 = st.pop() 
            op2 = st.pop() 
            st.append(op1+op2+ch)
    return st[-1]