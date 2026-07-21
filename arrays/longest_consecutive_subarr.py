def ls(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return True
    return False
def main(arr):
    n = len(arr)
    if n==0:
        return 0
    longst = 1
    for i in range(n):
        # [100, 4, 200, 1, 3, 2]  
        curr = arr[i]
        cnt = 1
        while ls(arr, curr+1):
            curr = curr+1
            cnt+=1
        longst = max(longst, cnt)
    return longst
def mainn(nums):
    n = len(nums)
    nums.sort() 
    if n==0:
        return 0
    cnt = 0
    max_len = 1
    for i in range(n):
        if i>0 and  nums[i] == nums[i-1]:
            continue
        elif i>0 and nums[i-1]+1 == nums[i]:
            cnt+=1
        else:
            cnt=1
        max_len = max(max_len, cnt)

    return max_len

def mainnn(arr):
    n = len(arr)
    s = set(arr)
    if n==0:
        return 0
    # cnt = 0
    max_len = 0
    for i in range(n):
        s.add(arr[i])
    for it in s:
        if it-1 not in s:
            cnt=1
            x = it
            while x+1 in s:
                cnt+=1
                x = x+1
            max_len = max(max_len, cnt)
    return max_len
    
if __name__ == "__main__":
    print(mainn([100, 4, 200, 1, 2, 3, 2]))