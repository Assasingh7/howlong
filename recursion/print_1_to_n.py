# forward recursion 
def main_f(count, n):
    if count > n:
        return 
    print(count)
    return main(count + 1, n)

# backward  recursion
def main_b(count, n):
    if count == 0:
        return
    main_b(count -1, n)
    print(count)
if __name__ == "__main__":
    main_b(7, 7) 