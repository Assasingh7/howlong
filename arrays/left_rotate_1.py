# def main(arr):
#     temp = [0]*len(arr)
#     var = arr[0]
#     for i in range(1, len(arr)):
#         temp[i-1] = arr[i]
#     temp[len(arr)-1] = var
#     for i in range(len(arr)):
#         arr[i] = temp[i]
#     return arr

# optimal
def main(arr):
    var = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[-1] = var
    
    return arr

if __name__ == "__main__":
   print(main([1, 2, 3, 4, 5]))
    