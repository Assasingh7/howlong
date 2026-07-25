class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def main(head):
    st = []
    temp = head
    while temp:
        st.append(temp.data)
        temp=temp.next
    temp = head
    while st:
        if st.pop() != temp.data:
            return False
        temp = temp.next

def reverse_list(head):
    if head is None or head.next is None:
        return head
    new  = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return new
def mmmain(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    new_head = reverse_list(slow.next)
    first = head
    sec = new_head
    while sec!=None:
        if first.data != sec.data:
            return False
        first = first.next
        sec = sec.next
    return True