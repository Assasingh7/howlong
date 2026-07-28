def expand_from_center(s, i, j):
    while i>= 0 and j<len(s) and s[i] == s[j]:
        i-=1
        j+=1
    return j-i-1
def main(s):
    start = 0
    end = 0
    for i in range(len(s)):
        odd = expand_from_center(s, i, i)
        even = expand_from_center(s, i, i+1)
        max_l = max(odd, even)
        if max_l>(end - start + 1):
            start = i-(max_l-1)//2
            end = i+max_l//2
    return s[start:end+1]
print(main("aba"))