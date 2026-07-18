def main(n):
    max_sum = 0
    if n == 0:
        return 0
    num = n%10
    max_sum = max(max_sum, num)
    max_sum = max(max_sum, main(n//10))

    return max_sum
if __name__ == "__main__":
    print(main(1234))