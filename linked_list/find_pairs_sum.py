class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class Main:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    def get_tail(self):
        if not self.head:
            return None
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr
    def print_list(self):
        curr = self.head
        res = []
        while curr:
            res.append(curr.data)
            curr = curr.next
        print("<->".join(res) if res else "Empty")
def main(dll, target_sum):
    pairs = []
    if not dll.head:
        return pairs
    left = dll.head
    right = dll.get_tail()
    while left and right and left !=right and left.prev!=right:
        curr_sum = left.data+right.data
        if curr_sum == target_sum:
            pairs.append((left.data, right.data))
            left = left.next
            right = right.prev
        elif curr_sum<target_sum:
            left = left.next
        else:
            right = right.prev
    return pairs