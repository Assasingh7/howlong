def is_ch(ch):
    return 'a'<=ch<='z'
def main(s, i):
    if i == len(s):
        return 0
    count = 0
    if is_ch(s[i]):
        count+=1
    count+=main(s, i+1)
    return count

if __name__ == "__main__":
    print(main("1ss1s2ss", 0))
