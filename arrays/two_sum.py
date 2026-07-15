from collections import defaultdict


def main(arr, target):
    n = len(arr)
    for i in range(n-1):
        for j in range(1, n):
            if arr[i]+arr[j] == target:
                return "YES"
    return "NO"

# def mainn(arr, target):
#     n = len(arr)
#     freq_map = defaultdict(int)
#     for i in range(n):
#         freq_map[arr[i]]=freq_map.get(arr[i], 0)+1
#     for i in range(n):
#         if target - arr[i] in freq_map:
#             return "YES"
#     return "NO"
def mainn(arr, target):
    n = len(arr)
    mp = {}
    for i, num in enumerate(arr):
        if target - arr[i] in mp:
            return "YES"
        mp[num] = i
    return "NO"

if __name__ == "__main__":
    print(mainn([2,6,5,12,11], 14))