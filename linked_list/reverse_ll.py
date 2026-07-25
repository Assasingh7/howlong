class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def main(head):
    st = []
    temp = head
    while temp:
        st.append(temp.data)
        temp = temp.next
    temp = head
    while len(st) != 0:
        temp.data = st.pop()
        temp = temp.next
    return head
def mainn(head):
    prev = None
    temp = head
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev
def maiin(head):
    if head is None or head.next is None:
        return head
    new  = maiin(head.next)
    head.next.next = head
    head.next = None
    return new
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = head.next.next
    a = maiin(head)
    while a:
        print(a.data)
        a = a.next
