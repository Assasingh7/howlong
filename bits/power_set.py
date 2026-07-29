def generate_subsequence(s, n):
    total = 1<<n
    ans = []
    for i in range(total):
        temp = []
        for j in range(n):
            if i & (1<<j):
                temp.append(s[j])
        ans.append("".join(temp))
    return ans
print(generate_subsequence("abc", 3))