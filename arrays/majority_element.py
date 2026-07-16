def main(arr):
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count+=1
        if count > n//2:
            return arr[i]
    return -1

def mmain(arr):
    n = len(arr)
    fre_mp = {}
    for i in range(n):
        fre_mp[arr[i]] = fre_mp.get(arr[i], 0)+1
    for k, v in fre_mp.items():
        if v > n//2:
            return k
    return -1
def mmm(arr):
    count=0
    elem = 0
    for num in arr:
        if count == 0:
            elem = num
            count+=1
        elif num!=elem:
            count-=1
        else:
            count+=1
    return elem

if __name__ == "__main__":
    print(mmm([7, 0, 0, 1, 7, 7, 2, 7, 7]))