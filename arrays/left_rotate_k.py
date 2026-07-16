def main(arr, k):
    n = len(arr)
    k%=n
    temp = []
    
    for i in range(k):
        temp.append(arr[k])
    for i in range(n):
