class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def main(head):
    temp = head
    mp = {}
    while temp:
        if temp in mp:
            return temp.data
        mp[temp] = 1
        temp = temp.next
    return None

def start_point(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow!=fast:
                slow = slow.next
                fast = fast.next
            return slow
            
    return None

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next.next
    print(start_point(head).data)
