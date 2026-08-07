def main(arr, goal):
    freq = {0:1}
    prefix = 0
    ans = 0

    for num in arr:
        prefix +=num
        need = prefix-goal
        ans+=freq.get(need, 0)
        freq[prefix] = freq.get(prefix, 0)+1
    return ans