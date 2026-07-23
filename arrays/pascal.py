def main( n):
    res = []
    for i in range(0, n):
        row = [1] * (i+1)
        for j in range(1, i):
            row[j] = res[i-1][j-1]+res[i-1][j]
        res.append(row)
    return res

def mmain(n):
    res = []
    val = 1
    res.append(val)

    for i in range(1, n):
        val = val * (n-i)//i
        res.append(val)
    return res

def mmmain( r, c):
    n = r - 1
    m = c - 1
    res = 1
    for i in range(m):
        res *= (n-i)
        res //= (i+1)
    return  res
print(mmmain( 5, 3))

    