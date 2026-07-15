def msin(arr):
    n = len(arr)
    sum_n = (n+1) * (n+2)//2
    sum = 0
    for i in range(n):
        sum += arr[i]
    return sum_n - sum 

def main(arr):
    n = len(arr)+1
    for i in range(1, n+1):
        found = False
        for j in range(n - 1):
            if arr[j] == i:
                found = True
                break
        if not found:
            return i

def mainn(arr):
    n = len(arr)+1
    xor1 = 0
    xor2 = 0
    for i in range(1, n+1):
        xor1^=i
    for i in range(n-1):
        xor2^=arr[i]
    return xor1^xor2


if __name__ == "__main__":
    print(mainn([8, 2, 4, 5, 3, 7, 1]))