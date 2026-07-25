class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def main(head):
    mp = {}
    timer = 0
    temp = head
    while temp:
        timer +=1
        if temp in mp:
            return timer- mp[temp] 
        mp[temp] = timer
        temp = temp.next
    return 0

def main_op(head):
    slow = head
    fast = head
    is_cycle = False
    cnt = 0
    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            is_cycle = True
            break
    if is_cycle:
        cnt = 1
        st = slow.next
        while st !=slow:
            cnt+=1
            st = st.next
        return cnt 
    return cnt 
if __name__ == "__main__":
    n = Node(3)
    n.next = Node(4)
    n.next.next = Node(5)
    n.next.next.next = Node(6)
    n.next.next.next.next = Node(7)
    n.next.next.next.next.next =  n.next.next.next
    n.next.next.next
    print(main_op(n))

