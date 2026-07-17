def main(arr):
    n = len(arr)
    leader = [arr[n - 1]]
    # print(leader)
    max_val = arr[n-1]
    for i in range(n-2, -1, -1):
        # print(arr[i], leader[j])
        if max_val < arr[i]:
            leader.append(arr[i])
            max_val = arr[i]
    leader.reverse()
    return leader

if __name__ == "__main__":
    print(main([4, 7, 1, 0])) 
