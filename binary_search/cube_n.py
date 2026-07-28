def main(n, m):
    l = 1
    h = m
    while l<=h:
        mid = l+(h-l)//2
        ans = 1
        for _ in range(n):
            ans *= mid
            if ans > m:
                break
        if ans == m:
            return mid
        elif ans<mid:
            l = mid+1
        else:
            h = mid-1
    return -1
print(main(3, 27))