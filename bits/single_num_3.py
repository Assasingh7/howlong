def main(arr):
    XOR = 0
    for i in range(len(arr)):
        XOR^=arr[i]
    right_most = (XOR&(XOR-1))^ XOR
    XOR1, XOR2 = 0, 0
    for i in range(len(arr)):
        if arr[i] & right_most:
            XOR1 = XOR1 ^ arr[i]
        else:
            XOR2 = XOR2 ^ arr[i]
    return [XOR1, XOR2] if XOR1<XOR2 else [XOR2, XOR1]

print(main([1, 1, 2, 2, 3, 5]))