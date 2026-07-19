class Node:
    def __init__(self, data, next=None):
        self.data = data       
        self.next = next 
def main(head):
    if head is None or head.next is None:
        return False
    mpp = {}
    temp = head
    while temp:
        if temp in mpp:
            return True
        mpp[temp] = 1
        temp = temp.next
    return False
def main_o(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow  = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False
if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # fifth.next = third
    print(main_o(head))
