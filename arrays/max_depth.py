def main(s):
    level = 0
    ans = 0
    for ch in s:
        if '(' in s:
            level+=1
        elif ')' in s:
            level-=1
        ans = max(ans, level)
    return ans
