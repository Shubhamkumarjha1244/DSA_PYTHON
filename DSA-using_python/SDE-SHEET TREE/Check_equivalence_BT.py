import class_level_wise_trasversal

def check_equivalence_BT(root_a,root_b):
    if root_a==None and root_b==None:
        return True
    if root_a==None or root_b==None:
        return False
    return root_a.data==root_b.data and check_equivalence_BT(root_a.left,root_b.left) and check_equivalence_BT(root_a.right,root_b.right)


tree=class_level_wise_trasversal.level_wise_trans()
root_a=tree.input_level_wise()
root_b=tree.input_level_wise()
print(check_equivalence_BT(root_a,root_b))



