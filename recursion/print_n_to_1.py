# def main(count, n):
#     if count == 0:
#         return
#     print(count)
#     main(count-1, n)
def main(count, n):
    if count > n:
        return
    main(count+1, n)
    print(count)

if __name__ == "__main__":
    main(0, 3)
