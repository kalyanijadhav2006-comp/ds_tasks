def get_bottom(stack):
    """Helper to pop and return the bottom element of the stack."""
    top = stack.pop()
    if not stack:
        
        return top
    else:
        bottom = get_bottom(stack)
        stack.append(top)  # push back other elements
        return bottom

def reverse_stack(stack):
    """Reverse the stack using recursion only."""
    if not stack:
        return
    
    bottom = get_bottom(stack)
    
    reverse_stack(stack)
    
    stack.append(bottom)


stack = [1, 2, 3, 4]
reverse_stack(stack)
print(stack)  # Output: [4, 3, 2, 1]