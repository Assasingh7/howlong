#  1
def reverse_arr(arr, i, j):
    if i > j:
        return
    arr[i], arr[j] = arr[j], arr[i]
    reverse_arr(arr, i+1, j-1)
# 2
def rev_arr_2(arr, i):
    n = len(arr)
    if i >= n//2:
        return
    arr[i], arr[n-i-1] = arr[n - i -1], arr[i]
    rev_arr_2(arr, i+1) 
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    # reverse_arr(arr, 0, len(arr) - 1)
    rev_arr_2(arr, 0)
    print(arr)