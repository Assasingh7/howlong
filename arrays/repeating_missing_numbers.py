def brute(arr):
    n = len(arr)
    repeating = -1, missing = -1
    for i in range(1, n+1):
        cnt = arr.count(i)
        if cnt == 2:
            repeating = i
        elif cnt == 1:
            missing = i
            if repeating !=-1 and missing !=-1:
                break
    return [repeating, missing]

def better(arr):
    hash_arr = [0]*(len(arr)+1)
    for a in arr:
        hash_arr[a]+=1
    
    repeating = -1, missing = -1
    for i in range(1, len(arr)+1):
        if hash_arr[i] == 2:
            repeating = i
        elif hash_arr[i] == 0:
            missing = i
    return [repeating, missing]

# def findMissingRepeatingNumbers(self, nums):
        
#         # Size of the array
#         n = len(nums)

#         # Sum of first n natural numbers
#         SN = (n * (n + 1)) // 2

#         # Sum of squares of first n natural numbers
#         S2N = (n * (n + 1) * (2 * n + 1)) // 6

#         """ Calculate actual sum (S) and sum 
#             of squares (S2) of array elements """
#         S = 0
#         S2 = 0
#         for num in nums:
#             S += num
#             S2 += num * num

#         # Compute the difference values
#         val1 = S - SN

#         # S2 - S2n = X^2 - Y^2
#         val2 = S2 - S2N

#         # Calculate X + Y using X + Y = (X^2 - Y^2) / (X - Y)
#         val2 = val2 // val1

#         """ Calculate X and Y from X + Y and X - Y
#             X = ((X + Y) + (X - Y)) / 2
#             Y = X - (X - Y) """
#         x = (val1 + val2) // 2
#         y = x - val1

#         # Return the results as [repeating, missing]
#         return [int(x), int(y)]
        
