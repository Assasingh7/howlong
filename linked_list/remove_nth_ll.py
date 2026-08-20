def main(head, N):
    dummy = Node(0, head)
    sl = dummy
    fst = dummy
    for _ in range(N+1):
        fst = fst.next
    while fst is not None:
        sl = sl.next
        fst = fst.next
    sl.next = sl.next.next
    return dummy.next