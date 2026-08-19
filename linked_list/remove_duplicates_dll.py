def main(head):
    curr = head
    while curr:
        newcurr = curr.next
        while newcurr and newcurr.data == curr.data:
            newcurr = newcurr.next
        curr.next = newcurr
        if newcurr:
            newcurr.prev = curr
        curr = curr.next
    return head