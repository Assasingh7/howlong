def main(s, i):
    ss = ''
    if i== len(s):
        return ''
    if s[i] != 'x':
        ss = ss+s[i]
    ss+= main(s, i+1)
    return ss
    
def move_to_end(sss):
    s = main(sss, 0)
    count = 0

    for j in range(len(sss)):
        if sss[j] == 'x':
            count+=1
    
    s+='x'*count
    return s
if __name__ == "__main__":
    print(main("abxx", 0))
    print(move_to_end("abxxb"))
