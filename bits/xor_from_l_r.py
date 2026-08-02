def main(l, r):
    ans = 0
    for i in range(l, r+1):
        ans ^=i
    return ans
def mainn(n):
    n = n%4
    if n == 1:
        return 1
    elif n == 0:
        return n
    elif n == 2:
        return n+1
    else:
        return 0
def ress(l, r):
    return mainn(l-1) ^ mainn(r)
