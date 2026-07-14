#  brute
def main(arr):
    n = len(arr)
    temp = [0]*n
    j = 0
    for i in range(n):
        if arr[i]!=0:
            temp[j] = arr[i]
            j+=1
    
    return temp

# Optimal
def move_zeroes(arr):
    j = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            i = j
            break
    
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j+=1
    
    return arr
            
if __name__ == "__main__":
    ar = move_zeroes([1 ,0 ,2 ,3 ,0 ,4 ,0 ,1])
    print(ar)