def main(n):
    binn = bin(n)[2:]
    return binn[-1] == '1'

def mainn(n):
    return n%2 == 1
print(main(8))