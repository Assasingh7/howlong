def brute(arr):
    n = len(arr)
    nums = []
    for i in range(n):
        if len(nums) ==0 and nums[0]!=arr[i]:
            cnt = 0
        
            for j in range(n):
                if arr[i] == arr[j]:
                    cnt+=1
            if cnt>n//3:
                nums.append(arr[i])
        if len(nums) == 2:
            return nums
    return []

def better(arr):
    n = len(arr)
    mp = {}
    res = []
    for i in range(arr):
        mp[arr[i]] = mp.get(arr[i], 0)+1
    
    for k, v in mp.items():
        if len(res) == 2:
            break
        if v>n//3:
            res.append(k)
    return res

def main(arr):
    cnt1 =  cnt2 = 0
    el1 =  el2 = None
    for num in arr:
        if cnt1 == 0 and num!=el2:
            el1 = num
            cnt1+=1
        elif cnt2 == 0 and num!=el1:
            el2 = num
            cnt2+=1
        elif num == el1:
            cnt1+=1
        elif num == el2:
            cnt2+=1
        else:
            cnt2-=1
            cnt1-=1
    cnt1 = 0
    cnt2 = 0

    for num in arr:
        if num == el1:
            cnt1 += 1
        elif num == el2:
            cnt2 += 1
    res = []
    mini = len(arr)//3+1
    if cnt1>=mini:
        res.append(el1)
    if cnt2>=mini and el1!=el2:
        res.append(el2)
    return res

        