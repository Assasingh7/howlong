def comb_sum(last,  temp,k,sum,  res):
    if sum == 0 and len(temp) == k:
        res.append(temp[:])
        return
    if sum<0 or len(temp)>k:
        return
    for i in range(last, 10):
        if i<=sum:
            temp.append(i)
            comb_sum(i+1,  temp, k, sum-i, res)
            temp.pop()
        else:
            break
    