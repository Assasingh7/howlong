def main(s, t):
    if len(s)!=len(t):
        return False
    if sorted(s) != sorted(t):
        return False
    return True

def mainn(s, t):
    if len(s)!=len(t):
        return False
    freq = [0]*26
    for ch in s:
        freq[ord(ch)-ord('A')]+=1
    for ch in t:
        freq[ord(ch)-ord('A')]-=1
    for i in freq:
        if i!=0:
            return False
    return True
