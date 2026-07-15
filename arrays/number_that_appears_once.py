from collections import defaultdict
def main(arr):
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1
        if count == 1:
            return arr[i]
    return -1

def mainn(arr):
    n = len(arr)
    freq_map = defaultdict(int)

    for i in range(n):
        freq_map[arr[i]] = freq_map.get(arr[i], 0) +1
    for k, v in freq_map.items():
        if v == 1:
            return k
    return -1
def mmaain(arr):
    n = len(arr)
    xor = 0
    for i in range(n):
        xor^=arr[i]
    return xor

if __name__ == "__main__":
    print(mmaain([2, 2, 1]))
                