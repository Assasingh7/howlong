import itertools
def main(arr):
    perm = sorted(set(itertools.permutations(arr)))
    curr = tuple(arr)
    for i in range(len(perm)):
        if perm[i] == curr:
            if i == len(perm) - 1:
                return list(perm[0])
            else:
                return list(perm[i+1])
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3]
    print(main(arr))