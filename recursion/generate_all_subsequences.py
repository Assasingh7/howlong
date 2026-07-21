def generate_bubsequence(s, i,n, temp, res):
    if i == n:
        if res == '':
            return
        temp.append(res)
        return temp
    generate_bubsequence(s, i+1, n,temp, res+s[i])
    generate_bubsequence(s, i+1, n,temp, res)
    return temp
print(generate_bubsequence("aa", 0, 2, [], ''))