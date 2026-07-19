class Node:
    def __init__(self, data, next=None):
        self.data = data       
        self.next = next  
def main(head):
    temp = head
    cnt = 0
    if head is None or head.next is None:
        return head
    while temp:
        cnt+=1
        temp = temp.next
    mid = head
    cnt = cnt // 2
    while cnt>0:
        mid = mid.next
        cnt-=1
    return mid.data

def main_o(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow  = slow.next
        fast = fast.next.next
    
    return slow
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print(main_o(head).data)



