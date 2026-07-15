def main(arr):
    count = 0
    maxi = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count = 0
        maxi = max(maxi, count)
        count +=1 
    return maxi
if __name__ == "__main__":
    print(main([1, 1, 0, 1, 1, 1]))