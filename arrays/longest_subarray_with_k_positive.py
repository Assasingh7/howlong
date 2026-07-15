def main(arr, k):
    n = len(arr)
    leng = 0
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for l in range(i, j+1):
                sum+=arr[l]
            if sum==k:
                leng = max(leng, j-i+1)
    return leng

def mainn(arr, k):
    n = len(arr)
    leng = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum+=arr[j]
            if sum==k:
                leng = max(leng, j-i+1)
    return leng
if __name__ == "__main__":
    print(mainn([10, 5, 2, 7, 1, 9], 15))