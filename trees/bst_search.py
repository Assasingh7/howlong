def main(rooot, target):
    if rooot.val == target:
        return rooot
    while rooot and rooot.val != target:
        if target<rooot.val:
            rooot = rooot.left
        else:
            rooot = rooot.right
    return rooot