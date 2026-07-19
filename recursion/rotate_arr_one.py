# [1, 2, 3, 4]
# [2, 3, 4, 1]
def main(arr, i, temp):
    if i==len(arr)-1:
        temp[-1] = arr[0]
        return temp
    if i<=len(arr)-2:
        temp[i] = arr[i+1]
    return main(arr, i+1, temp)
if __name__ == "__main__":
    m = main([1, 2, 3, 4, 5], 0, [0]*5)
    print(m)