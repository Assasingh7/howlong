# def main(arr, i, temp, res):
#     if i==len(arr):
#         res.append(temp[:])
#         return
#     temp.append(arr[i])
#     main(arr, i+1, temp, res)
#     temp.pop()
#     main(arr, i+1, temp, res)
#     return
# # def main_unique()

# arr = [1, 2]
# n = len(arr)
# temp = []
# main(arr, 0,[], temp)
# temp.sort()
# print(temp)

def main(arr, i, temp, res):
    if i==len(arr):
        res.add(tuple(temp))
        return
    temp.append(arr[i])
    main(arr, i+1, temp, res)
    temp.pop()
    main(arr, i+1, temp, res)
    return
def main_unique(arr):
    ds = []
    ans = set()
    arr.sort()
    main(arr, 0, ds, ans)
    return [list(subset) for subset in ans]

arr = [1, 2]
# n = len(arr)
# temp = []
# main(arr, 0,[], temp)
# temp.sort()
# print(temp)
print(main_unique(arr))