class  Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
        
class Sol:
    def insert(self, data, head):
        if head is None:
            return Node(data)
        node = Node(data)
        node.next = head
        return node
    def insert_at_end(self, data, head):
        if head is None:
            return None(data)
        curr = head
        while curr.next:
            curr = curr.next
        node  = Node(data)
        curr.next = node
        node.prev = curr
        return head
    def delete_at_end(self, head):
        if head is None or head.next is None:
            return None
        cur = head
        while cur.next:
            cur = cur.next
        cur.prev.next = None

        return head
    
    def reverse_dll(self, head):
        if head is None:
            return head
        curr = head
        temp = None 
        while curr is not None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        
        if temp is not  None:
            head = curr.prev
        return head

        

if __name__ == "__main__":
    sol = Sol()
    node = Node(3)
    i_node = node(4)
