def main(arr):
    arr.sort()
    first = arr[0]
    last = arr[-1]
    ans = []
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return "".join(ans)
        ans.append(first[i])
    return "".join(ans)

print(main(["flower", "flow", "flight"]))