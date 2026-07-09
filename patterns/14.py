# A 
# B C 
# D E F 
# G H I J 
# K L M N O 
def main(n):
    count = 0
    for i in range(n):
        for _ in range(i+1):
            print(chr(65+count), end=" ")
            count +=1
        print()

if __name__ == "__main__":
    main(5)