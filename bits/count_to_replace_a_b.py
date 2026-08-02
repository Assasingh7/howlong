def main(a, b):
    xor = a^b
    count = 0
    while xor:
        count+=xor&1
        xor=xor>>1
    return count
print(main(10, 7))