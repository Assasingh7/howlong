def main(s):
    st = []
    for i in range(s):
        if s[i] in '({[':
            st.append(s[i])
        else:
            if not st:
                return False
            val = st.pop()
            if (val == '(' and s[i] == ')') or (val == '{' and s[i] == '}') or (val == '[' and s[i] == ']'):
                continue
            else:
                return False
    return not st
