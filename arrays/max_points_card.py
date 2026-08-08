def main(arr, k):
    left_sum = sum(arr[:k])
    right_sum = 0
    max_sum = left_sum
    for i in range(k-1, -1, -1):
        print("i",i)
        left_sum-=arr[i]
        print(len(arr)-(k-i))
        right_sum+=arr[len(arr)-(k-i)]
        max_sum = max(max_sum, left_sum+right_sum)
    return max_sum
print(main([1, 2, 3, 4, 5, 6], 3))