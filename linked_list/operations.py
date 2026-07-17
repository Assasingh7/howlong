class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def insert_head(self, head, new_data):
        node = Node(head, new_data)
        return node
    def delete_at_end(self, head):
        if head is None or head.next is None:
            return None
        curr = head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
        return head

    def print_list(self, head):
        temp = head
        while temp:
            print(temp.data, "->", end="")
            temp=temp.next
        print( end="")

    def length_of_ll(self, head):
        cnt = 0
        temp = head
        while temp:
            cnt+=1
            temp = temp.next
        return cnt
    def search(self, head, target):
        if head.data == target:
            return True
        curr = head
        while curr:
            if curr.data == target:
                return True
            curr = curr.next
        return False
if __name__ == "__main__":
    head = Node(3)
    b = Solution().insert_head(4, head)
    # Solution().print_list(b)
    c = Solution().delete_at_end(b)
    Solution().print_list(c)