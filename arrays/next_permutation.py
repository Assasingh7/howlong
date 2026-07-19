import itertools
def main(arr):
    perm = sorted(set(itertools.permutations(arr)))
    curr = tuple(arr)
    for i in range(len(perm)):
        if perm[i] == curr:
            if i == len(perm) - 1:
                return list(perm[0])
            else:
                return list(perm[i+1])
    return arr

def mainn(arr):
    index = -1
    n = len(arr)
    for i in range(n-2, -1, -1):
        if arr[i]<arr[i+1]:
            print(i, i+1)
            index = i
            break
    if index == -1:
        arr.reverse()
        return
    for i in range(n-1, index, -1):
        if arr[i]>arr[index]:
            print("a", i, index)
            arr[i], arr[index] = arr[index], arr[i]
            break
    arr[index+1:] = reversed(arr[index+1:])
    return
if __name__ == "__main__":
    arr = [1, 2, 3]
    mainn(arr)
    print(arr)