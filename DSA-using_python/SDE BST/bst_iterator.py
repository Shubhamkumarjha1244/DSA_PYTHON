import class_level_wise_trasversal


class BSTIterator:

    def __init__(self, root):
        self.st=[]
        curr=root
        while curr!=None:
            self.st.append(curr)
            self.start=curr
            curr=curr.left

    def next(self) -> int:
        node=self.st.pop()
        if node.right:
            right=node.right
            while right!=None:
                self.st.append(right)
                right=right.left
        return node.data

    def hasNext(self) -> bool:
        return len(self.st)!=0


bst=class_level_wise_trasversal.level_wise_trans()
root=bst.input_level_wise()
sol=BSTIterator(root)
bst.print_tree_levelwise(root)
print(sol.next())
print(sol.next())
print(sol.next())
print(sol.next())
print(sol.next())
print(sol.hasNext())

