def main(arr):
    n= len(arr)
    pos = []
    neg = []
    res = [0]*n
    for i in range(n):
        if arr[i]>=0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    for i in range(n//2):
        arr[2*i] = pos[i]
        arr[2*i+1] = neg[i]
    return arr
def mainn(arr):
    n = len(arr)
    res = [0]*n
    neg_idx = 1
    pos_idx = 0
    for i in range(n):
        if arr[i]>=0:
            res[pos_idx] = arr[i]
            pos_idx+=2
        else:
            res[neg_idx] = arr[i]
            neg_idx+=2
    return res

if __name__ == "__main__":
    print(mainn([1, 2, -4, -5]))        
