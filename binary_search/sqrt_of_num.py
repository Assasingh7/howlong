def main(n):
    lo = 1
    high = n
    while lo<=high:
        mid = lo+(high - lo)//2
        if mid*mid == n:
            return mid
        elif mid <= n//mid:
            lo = mid+1
        else:
            high = mid - 1
    return high
print(main(5))