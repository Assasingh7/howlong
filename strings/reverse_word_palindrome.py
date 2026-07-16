def main(word):
    temp = word.strip().split(' ')
    n = len(temp)
    rev = [""] * n
    for i in range(n):
        rev[n - i -1] = temp[i]

    
    return  " ".join(rev)
def mmsin(word):
    n =len(word)
    i = n-1
    s = ""
    end = 0
    while i>=0:
        while i>=0 and word[i] == " ":
            i-=1
        if i<0:
            break
        end = i
        while i>=0 and word[i] != " ":
            i-=1
        sub_str = word[i+1:end+1]
        if s!="":
            s+= " "
        s+=sub_str
    return s
        
if __name__ == "__main__":
    print(mmsin("welcome to the jungle"))
