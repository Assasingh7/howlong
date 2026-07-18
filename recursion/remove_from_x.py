def main(s, i=0):
    ss = ""
    if i==len(s):
        return ss
    if s[i] != 'x':
        ss = s[i]+main(s, i+1)
    else:
        ss += main(s, i+1) + 'x'
    return ss

if __name__ == "__main__":
    print(main("abxxxab", 0))

