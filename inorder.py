def inorderTraversal(root, visitfn):
    # the strategy is to use recursive

    result = []
    
    # always search root.left first, if root.left.left is none, return root.left.value
    # [left.value].append(root.value)
    # [left.value, root.value].append(root.right.value)
    # recursive left, root, recursive right
    
    if root:
        result = inorderTraversal(root.left, visitfn)
        result.append(visitfn(root))
        result = result + inorderTraversal(root.right, visitfn)

    return result

def visitfn(root):
    # can be modified
    # return the value of every node

    return root.value
