def main(s, t):
    if len(s)!=len(t):
        return False
    mpp = {}
    rev = {}
    for i in range(len(s)):
        if s[i] in mpp and mpp[s[i]] != t[i]:
            return False
        if t[i] in rev and rev[t[i]] != s[i]:
            return False
        mpp[s[i]]= t[i]
        rev[t[i]]= s[i]
    return True
print(main("foo", "bar"))
