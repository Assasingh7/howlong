def main(n, x):
    ans = 1
    # l = abs(x)
    temp = x
    if x<0:
        n = 1/n
        temp = -1 * x 
    for _ in range( temp):
        ans*=n
    return ans

def mainn(x, n): #x^n
    if n == 0:
        return 1
    if n<0:
        x=1/x
        n = -1*n

    return x*main( x, n-1)

def mainnn(x, n): #x^n
    if n == 0:
        return 1.0
    if n == 1:
        return x
    if n%2 == 0:
        return mainn(x*x, n//2)
    return x*main( x, n-1)
    
def pow(x, n):
    if n<0:
        return 1.0/mainnn(x,- n)
    return mainnn(x, n)
print(main(2.000, -2))
print(pow(  2.0000, -2))
