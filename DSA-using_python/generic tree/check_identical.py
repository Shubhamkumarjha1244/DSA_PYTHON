import class_generic_tree

def check_identical(r1,r2):
    if r1==None and r2==None:return True
    if r1==None or r2==None:return False
    if len(r1.children)!=len(r2.children):return False
    i=0
    identical=True
    while i<len(r1.children) and i<len(r2.children):
        identical=(identical and check_identical(r1.children[i],r2.children[i]))
        i+=1
    return (r1.data==r2.data) and identical


gt=class_generic_tree.generic_tree_class()
r1=gt.level_wise_input()
r2=gt.level_wise_input()
print(check_identical(r1,r2))


    

    
