#  singly
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

#  doubly
class DoubleNode:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

if __name__ == "__main__":
    arr = [2, 5, 8, 7]
    print(Node(arr[0]))
    print(Node(arr[0]).data)
    print(Node(arr[0]).next)

        
    