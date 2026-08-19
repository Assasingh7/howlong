def main(head, k):
    curr = head
    while curr:
        if curr.data == k:
            if curr==head:
                curr= curr.next
                if head:
                    head.prev=None
            else:
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
        curr = curr.next
    return head