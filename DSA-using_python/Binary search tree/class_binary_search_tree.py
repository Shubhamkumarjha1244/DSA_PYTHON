
import queue


class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None

class bst:
    def __init__(self):
        self.root=None
        self.count=0
    def balance_bst(self):
        pass

    def print_bst_helper(self,root):
        if root==None:return
        qu=queue.Queue()
        qu.put(root)
        while qu.empty()==False:
            node=qu.get()
            print(node.data,end=' : ')
            if node.left:
                qu.put(node.left)
                print('left node :',node.left.data,end=' ')
            if node.right:
                qu.put(node.right)
                print('right node :',node.right.data,end=' ')
            print()
        

    def print_bst(self):
        self.print_bst_helper(self.root)  

    def count_bst(self):
        return self.count
    
    def insert_bst_helper(self,root,val):
        if root==None:
            root=Node(val)
            return root
        if root.data>val:
            root.left=self.insert_bst_helper(root.left,val)
        else:
            root.right=self.insert_bst_helper(root.right,val)
        return root

    def insert_bst(self,val):
        self.root=self.insert_bst_helper(self.root,val)
        self.count+=1
    def delete_node(self,root):
        if root==None:return
        if root.left==None and root.right==None :return
        if root.left==None or root.right==None :
            if root.left:return root.left
            else:return root.right
        else:
            root=root.right
            root.right=self.delete_node(root.right)
            return root
    def delete_bst_helper(self,root,val):
        if root==None: return root
        if root.data==val:
            root=self.delete_node(root)
        if root.data>val:
            self.delete_bst_helper(root.left,val) 
        else:
            self.delete_bst_helper(root.right,val)



    def delete_bst(self,val):
        self.delete_bst_helper(self.root,val)
    def search_bst_helper(self,root,val):
        if root==None:return -1
        elif root.data==val: return val
        elif root.data > val: return self.search_bst_helper(root.left,val)
        elif root.data < val: return self.search_bst_helper(root.right,val)



    def search_bst(self,val):
       return self.search_bst_helper(self.root,val)
        


bst1=bst()
bst1.insert_bst(1)
bst1.insert_bst(2)
bst1.insert_bst(9)
bst1.insert_bst(10)
bst1.insert_bst(11)
bst1.insert_bst(15)
bst1.insert_bst(7)
bst1.insert_bst(4)
bst1.print_bst()
print()
print(bst1.search_bst(6))
print(bst1.count_bst())
print('------')
bst1.delete_bst(9)
bst1.print_bst()