MOD = 10**9+7
def main(n, index):
    if index == n:
        return 1
    res = 0
    if index%2==0:
        even = [0, 2, 4, 6, 8]
        for digit in even:
            res=(res+main(n, index+1))%MOD
    else:
        prime = [2,3, 5, 7]
        for digit in prime: 
            res=(res+main(n, index+1))%MOD
    return res

if __name__ == "__main__":
    n = 1
    print(main(n, 0))
