from collections import defaultdict
# brute force
def main(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    union = []
    freq_map = defaultdict(int)
    for i in range(n):
        freq_map[arr1[i]] = freq_map.get(arr1[i], 0) + 1
    for i in range(m):
        freq_map[arr2[i]] = freq_map.get(arr2[i], 0) + 1
    for key, _ in freq_map.items():
        
        union.append(key)

    union.sort()
    return union

# better 
def main_b(arr1, arr2):
    st = set(arr1) | set(arr2)
    return st

#  OPTIMAL
def mainn(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = 0
    j = 0
    union = []
    while i<n and j<m:
        if arr1[i] < arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1
        else:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
            j+=1
    while i<n:
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i+=1
    while j<m:
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j+=1
    return union


if __name__ == "__main__":
    arr1 = [1,2,3,4,5]
    arr2 = [2, 3, 4, 5]
    print(mainn(arr1, arr2))
