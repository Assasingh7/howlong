def main(n):
    cnt = 0
    while(n):
        if n&1:
            cnt+=1
        n>>1
    return cnt

def main(n):
    cnt = 0
    while(n):
        cnt+=1
        n = n&(n-1)
    return cnt

