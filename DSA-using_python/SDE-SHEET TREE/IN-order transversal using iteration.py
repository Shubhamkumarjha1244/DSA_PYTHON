import class_level_wise_trasversal

def In_order_transversal_using_iteration(root):
    curr=root
    while curr:
        if not(curr.left):
            print(curr.data,end=' ')
            curr=curr.right
        else:
            prev=curr.left
            while prev.right and prev.right!=curr:
                prev=prev.right
            if prev.right==None:
                prev.right=curr
                curr=curr.left
            else:
                prev.right=None
                print(curr.data,end=' ')
                curr=curr.right

def Pre_order_transversal_using_iteration(root):
    curr=root
    while curr:
        if not(curr.left):
            print(curr.data,end=' ')
            curr=curr.right
        else:
            prev=curr.left
            while prev.right and prev.right!=curr:
                prev=prev.right
            if prev.right==None:
                prev.right=curr
                print(curr.data,end=' ')
                curr=curr.left
            else:
                prev.right=None
                curr=curr.right




# def in_order(root): 
#     curr=root
#     while curr:
#         if curr.left==None:
#             print(curr.data,end=' ')
#             curr=curr.right
#         else:
#             prev=curr.left
#             while prev.right and prev.right!=curr:
#                 prev=prev.right
#             if prev.right==None:
#                 prev.right=curr
#                 curr=curr.left
#             else:
#                 prev.right=None
#                 print(curr.data,end=' ')
#                 curr=curr.right













tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
In_order_transversal_using_iteration(root)
print()
Pre_order_transversal_using_iteration(root)

# in_order(root)