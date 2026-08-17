def main(head):
    oddHead  = None
    oddTail = None
    evenHead = None
    evenTail = None
    curr = head
    while curr:
        if curr.val % 2 == 0:
            if evenHead is None:
                evenHead = curr
                evenTail = curr
            else:
                evenTail.next = curr
                evenTail = curr
        else:
            if oddHead is None:
                oddHead = curr
                oddTail = curr
            else:
                oddTail.next = curr
                oddTail = curr
        curr = curr.next
    if evenHead is None:
        return oddHead
    if oddHead is None:
        return evenHead
    evenTail.next = oddHead
    oddTail.next = None
    return evenHead