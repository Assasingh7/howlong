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
def mmain(arr, k):
    n = len(arr)
    l =  r = 0
    length = 0 
    sum = 0
    while r<n:
        sum += arr[r]
        while sum>k:
            sum -= arr[l]
            l+=1
        if sum==k:
            length = max(length, r-l+1)
        r+=1
    return length

if __name__ == "__main__":
    print(mmain([10, 5, 2, 7, 1, 9], 15))