def _is_num(ch):
    return '0'<=ch<='9'

def main(s, i):
    if i>=len(s):
        return True
    if not _is_num(s[i]):
        return False
    return main(s, i+1)
if __name__ == "__main__":
    print(main("1s23", 0))