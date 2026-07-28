def main(s):
    tot = 0
    for i in range(len(s)):
        fre = {}
        for j in range(i, len(s)):
            fre[s[j]] = fre.get(s[j], 0)+1
            maxx = max(fre.values())
            minn = min(fre.values())
            tot+=(maxx-minn)
    return tot
print(main("aabcbaa"))