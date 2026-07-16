def main(arr, k):
    n = len(arr)
    k%=n
    temp = []
    temp_2 = arr[:]
    
    for i in range(n-k, n):
        temp.append(arr[i])
    for i in range(n-k):
        print(i+k)
        arr[i+k] = temp_2[i]
    # print(temp)
    for i in range(k):
        arr[i] = temp[i]
    return arr
def reverse(arr, i, j):
    while i<j:
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
def mmain(arr, k):
    n = len(arr)

    if n==0 or k==0:
        return arr
    reverse(arr, 0, n-1)
    reverse(arr,0, k-1)
    reverse(arr,k, n-1)
    return arr
if __name__ == "__main__":
    print(mmain([1, 2, 3, 4, 5, 6, 7], 2))
