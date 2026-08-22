import math


def calcTH(piles, speed):
    totH = 0
    for i in piles:
        totH+=math.ceil(i/speed)
    return totH
def main(piles, h):
    maxP = max(piles)
    l, h=1, maxP
    ans = maxP
    while l<=h:
        m = (l+h)//2
        totH = calcTH(piles, m)
        if totH<=h:
            ans = m
            h = m-1
        else:
            l = m+1
    return ans