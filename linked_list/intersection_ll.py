def main(headA, headB):
    if not headA or headB:
        return None
    node_a = set()
    curr_a = headA
    while curr_a:
        node_a.add(curr_a)
        curr_a = curr_a.next
    curr_b = headB
    while curr_b:
        if curr_b in node_a:
            return curr_b
        curr_b = curr_b.next
    return None
def main_op(head_a, head_b):
    if not head_a or head_b:
        return None
    pt_a = head_a
    pt_b = head_b
    while pt_a!=pt_b:
        pt_b = head_a if pt_b else pt_b.next
        pt_a = head_b if pt_a else pt_a.next
    return pt_a
