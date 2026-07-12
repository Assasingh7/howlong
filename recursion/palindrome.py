def main(s, i):
    n = len(s)
    if i>=n//2:
        return True
    if s[i].isalnum() != s[n - i - 1].isalnum():
        return False
    return main(s, i+1)

if __name__ == "__main__":
    s = main("assa", 0)
    print(s)