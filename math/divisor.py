def list_all_divisors(n):
    arr = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            arr.append(i)
        if n // i != i:
            arr.append(n // i)

    return arr
if __name__ == "__main__":
    print(list_all_divisors(10))