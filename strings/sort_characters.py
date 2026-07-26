def main(s):
    hash_arr = [(0, (i+ord('a'))) for i in range(26)]
    # result = []
    for ch in s:
        c_h = ord(ch) - ord('a')
        hash_arr[c_h] = (hash_arr[c_h][0]+1, ch)
    hash_arr.sort(key=lambda x: (-x[0], x[1]))
    result = [ch for f, ch in hash_arr if f>0]
    return result

print(main('tree'))