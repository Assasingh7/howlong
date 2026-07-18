def main(arr):
    n = len(arr)
    max_p = float('-inf')
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]< arr[j]:
                max_p = max(max_p, arr[j] - arr[i])
            
    return max_p
def main_optimal(arr):
    n = len(arr)
    max_profit = 0
    min = float('inf')
    for i in range(n):
        if arr[i]<min:
            min = arr[i]
        max_profit = max(max_profit, arr[i]-min)
    return max_profit

if __name__ == "__main__":
    arr = [7,1,5,3,6,4]
    print(main_optimal(arr))