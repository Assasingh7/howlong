def main(dividend, divisor):
    if dividend == divisor:
        return 1
    if dividend == -2**31 and divisor == -1:
        return 2**31  - 1
    if divisor == 1:
        return dividend
    isPos = True
    if dividend>=0 and divisor<0:
        isPos = False
    if dividend<0 and divisor>0:
            isPos = False
    n = abs(dividend)
    d = abs(divisor)
    ans = 0
    sum_ = 0
    while sum_+d<=n:
        ans+=1
        sum_+=d
    if ans > 2**31 - 1 and isPos:
        return 2**31 - 1
    if ans > 2**31 - 1 and not isPos:
        return -2**31
    return ans if isPos else -1*ans