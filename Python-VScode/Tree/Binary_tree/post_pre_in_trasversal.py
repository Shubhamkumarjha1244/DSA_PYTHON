class treeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def generateTree():
    val=int(input())
    if val==-1:return
    root=treeNode(val)
    root.right=generateTree()
    root.left=generateTree()
    return root

def PreTransversal(root):
    if root==None:return
    print(root.data)
    PreTransversal(root.right)
    PreTransversal(root.left)


def PostTransversal(root):
    if root==None:return
    PostTransversal(root.right)
    PostTransversal(root.left)
    print(root.data)

def InTransversal(root):
    if root==None:return
    InTransversal(root.right)
    print(root.data)
    InTransversal(root.left)


root=generateTree()
print('-------Post Tranversal------')
PostTransversal(root)
print('-----PreTransversal--------')
PreTransversal(root)
print('-------Intransversal------')
InTransversal(root)
