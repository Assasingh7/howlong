def main(arr):
    n = len(arr)
    pre, suff = 1, 1
    max_sum = float('-inf')
    for i in range(n):
        if pre==0:
            pre = 1
        if suff==0:
            suff = 1
        pre *= arr[i]
        suff *= arr[n-i-1]
        max_sum = max(max_sum, pre, suff)
    return max_sum
print(main([1, 2, 3, 0, -4, -5]))
# def maxProduct(self, nums):
#         res = nums[0]
#         maxProd = nums[0]
#         minProd = nums[0]

#         for i in range(1, len(nums)):
#             curr = nums[i]

#             if curr < 0:
#                 maxProd, minProd = minProd, maxProd

#             maxProd = max(curr, maxProd * curr)
#             minProd = min(curr, minProd * curr)
#             res = max(res, maxProd)
