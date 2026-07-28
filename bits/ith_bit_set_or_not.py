def main(n, i):
    return (n & (1<<i))!=0
def mainn(n, i):
    binn = bin(n)[2:]
    if i>=len(binn):
        return False
    return binn[-(i+1)] == '1'