def main(s1, s2, i, j):
    if i == len(s1) and j == len(s2):
        return True
    if s1[i]!=s2[j]:
        return False
    return main(s1, s2, i+1, j+1)

if __name__ == "__main__":
    s1 = "aaa"
    s2 = "aba"
    if len(s1)!= len(s2):
        print(False)
    print(main(s1, s2, 0, 0))