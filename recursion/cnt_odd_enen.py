def main_even(arr, i):
    cnt = 0
    if i == len(arr):
        return 0
    if arr[i]%2 == 0:
        cnt+=1
    return cnt+main_even(arr, i+1)
def main_odd(arr, i):
    cnt = 0
    if i == len(arr):
        return 0
    if arr[i]%2 == 1:
        cnt+=1
    return cnt+main_odd(arr, i+1)
if __name__ == "__main__":
    o = main_odd([1, 2, 3, 4, 5, 6], 0)
    e = main_even([1, 2, 3, 4, 5, 6], 0)
    print(o, e)