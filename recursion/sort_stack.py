def sort_stack(stack):
    if stack:
        temp = stack.pop()
        sort_stack(stack)
        insert_stack(stack, temp)
def insert_stack(stack, temp):
    # if not stack:
    if not stack or stack[-1]>=temp:
        stack.append(temp)
        return
    val = stack.pop()
    insert_stack(stack, temp)
    stack.append(val)

stk = [1, 2, 3]
print(sort_stack(stk))
print(stk)