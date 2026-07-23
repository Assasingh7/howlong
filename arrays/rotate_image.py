def main(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(len(arr)):
        arr[i].reverse()
    return arr
