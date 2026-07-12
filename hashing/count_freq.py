# brute force
from collections import defaultdict


def main(arr):
    n = len(arr)
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        count = 1
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                count += 1
                visited[j] = True
        
        print(arr[i], count)
# Optimal
def using_hash(arr):
    n = len(arr)
    map = defaultdict(int)
    for i in range(n):
        map[arr[i]] += 1
    for key, value in map.items():
        print(key, value)
if __name__ == "__main__":
    # main([10, 5, 10, 15, 10, 5])
    using_hash([10, 5, 10, 15, 10, 5])

