def main(arr):
    n = len(arr)
    max_sum = float("-inf")
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j+1):
                sum+=arr[k]
            max_sum = max(max_sum, sum)
    return max_sum

def mainn(arr):
    n = len(arr)
    max_sum = float("-inf")
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum+=arr[j]
            max_sum = max(max_sum, sum)
    return max_sum
def kadane(arr):
    n = len(arr)
    max_sum = float('-inf')
    s = 0
    for i in range(n):
        s +=arr[i]
        if s<0:
            s = 0
        max_sum = max(max_sum, s)
    return max_sum
def kadane_arrr(arr):
    n = len(arr)
    sum = 0
    strt = 0
    ans_strt = -1
    ans_end = -1
    max_sum = float('-inf')
    for i in range(n):
        sum+=arr[i]
        if sum < 0:
            strt = i
        if sum> max_sum:
            max_sum = sum
            ans_strt = strt
            ans_end = i
    return arr[ans_strt:ans_end+1]

if __name__ == "__main__":
    print(kadane_arrr([2, 3, 5, -2, 7, -4]))
            
