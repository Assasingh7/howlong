def is_armstrong_number(n):
    k = len(str(n))
    num = n
    arm_num = 0
    while num != 0:
        arm_num += (num%10) ** k
        num //= 10
    return arm_num == n
if __name__ == "__main__":
    is_armstrong_num = is_armstrong_number(153)
    print(is_armstrong_num) 