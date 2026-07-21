def genrate_b_strings(s, n, temp):
    if len(s) == n:
        temp.append(s)
        return temp
    genrate_b_strings(s+'0',n, temp)
    if s==''  or s[-1]=='0':
        genrate_b_strings(s+'1', n, temp)
    return temp

print(genrate_b_strings('', 3, []))