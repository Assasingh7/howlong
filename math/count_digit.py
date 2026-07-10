import math

#  Brute force
def count_digits(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count

# Optimal
def count_digit(n):
    if n == 0:
        return 1
    return int(math.log10(n)) + 1
if __name__ == "__main__":
    # print(count_digits(1234))
    print(count_digit(1234))
