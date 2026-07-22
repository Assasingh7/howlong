mpp = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv" ,"wxyz"]
def main( ind, digits, current, res):
    if ind == len(digits):
        res.append(current)
        return
    s= mpp[int(digits[ind])]
    for ch in s:
        main( ind+1, digits, current+ch, res)
        