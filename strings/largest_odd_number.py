# def main(s):
#     num = int(s)
#     new_str = str(num)
#     i = len(new_str) -1
#     while i>=0:
#         if int(new_str[i]) % 2 == 1:
#             break
#         i-=1
#     return new_str[0:i+1]
def main(s):
    i = len(s) - 1
    while i>=0:
        if int(s[i])%2==1:
            return s[:i+1].lstrip('0') or '0'
        i-=1
print(main("0023578"))
