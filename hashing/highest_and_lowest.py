# brute force
from collections import defaultdict


def main(arr):
    n = len(arr)
    visited = [False]*n
    maxFreq = 0
    minFreq = n
    maxElem = 0
    minElem = 0

    for i in range(n):
        if visited[i]:
            continue
        count = 1
        for j in range(i+1, n):
            if arr[i]==arr[j]:
                count += 1
                visited[j] = True
        if count > maxFreq:
            maxElem = arr[i]
            maxFreq = count
        if count < minFreq:
            minElem = arr[i]
            minFreq = count
    print(maxElem, minElem)
#  Optimal
def main_map(arr):
    n = len(arr)
    maxFreq = 0
    minFreq = n
    maxElem = 0
    minElem = 0

    freq_map = defaultdict(int)
    for i in range(n):
        freq_map[arr[i]]+=1
    for key, val in freq_map.items():
        if val > maxFreq:
            maxElem = key
            maxFreq = val
        if val < minFreq:
            minElem = key
            minFreq = val
    print(maxElem, minElem)

if __name__ == "__main__":
    main_map([2,2,3,4,4,2])
            

