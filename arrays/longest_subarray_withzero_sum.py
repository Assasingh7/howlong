def main(arr):
    n = len(arr)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j+1):
                sum+=arr[k]
            if sum==0:
                max_len = max(max_len, j-i+1)
    
    return max_len

def main(arr):
    n = len(arr)
    max_len = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum+=arr[j]
            if sum==0:
                max_len = max(max_len, j-i+1)
    
    return max_len
def mainn(arr):
    n = len(arr)
    pref_sum = {}
    sum = 0
    max_len = 0
    for i in range(n):
        sum += arr[i]
        if sum == 0:
            max_len = i+1
            return max_len
        else:
            if sum in pref_sum:
                max_len = max(max_len, i-pref_sum[sum])
            else:
                pref_sum[sum] = i
    return max_len
if __name__ == "__main__":
    print(mainn([9, -3, 3, -1, 6, -5]))
                

