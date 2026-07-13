# brute (misses repetitive case)
def main(arr):
    n = len(arr)
    if n == 0 or n ==1:
        return [-1, -1]
    arr.sort()
    return [arr[1], arr[n-2]]    
# better
def main_f(arr):
    n = len(arr)
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
    
    for i in range(n):
        if arr[i] < second_small and arr[i]!=small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i]!=large:
            second_large = arr[i]
    return [second_small, second_large]
# optimal
def main_s(arr):
    n = len(arr)
    if n<2:
        return -1
    sec_small = second_smallest(arr)
    sec_large = second_largest(arr)
    return sec_small, sec_large
def second_smallest(arr):
    n = len(arr)
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if arr[i]<small:
            second_small = small
            small = arr[i]
        elif arr[i]<second_small and arr[i]!=small:
            second_small = arr[i]
    return second_small

def second_largest(arr):
    n = len(arr)
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if arr[i]>large:
            second_large = large
            large = arr[i]
        elif arr[i]>second_large and arr[i]!=large:
            second_large = arr[i]
    return second_large
if __name__ == "__main__":
    arr = [1, 2, 4, 7, 7, 5]
    a, b = main_s(arr)
    print(a, b)