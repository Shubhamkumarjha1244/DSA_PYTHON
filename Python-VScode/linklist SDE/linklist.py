class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def inputLL():
    inputList=[1,2,3,4,-1]


    # inputList=[int(ele) for ele in input().split()]
    head=None
    tail=None

    for curr in inputList:
        if curr == -1:
            break

        newNode=Node(curr)

        if head is None:
            head=newNode
            tail=head
        else:
            tail.next=newNode
            tail=newNode

    return head


def printLL(head):
    while head:
        print(head.data,end='->')
        head=head.next

def lengthLL(head):
    count=0
    while head:
        count +=1
        head=head.next
    return count

def insertLL(head,pos,data):
    if pos <0 or pos > lengthLL(head):
        return head
    
    prev=None
    curr=head
    count=0
    newnode=Node(data)

    while count <pos:
        prev=curr
        curr=curr.next
        count +=1
    
    if prev is None:
        newnode.next=head
        head=newnode
    else:
        prev.next=newnode
        newnode.next=curr
    return head

def deleteLL(head,pos):
    if pos < 0 or pos > lengthLL(head):
        return head
    
    prev=None
    curr=head
    count=0
    while count < pos :
        prev=curr
        curr=curr.next
        count +=1

    if prev is None:
        curr=curr.next
        head=curr
    else:
        curr=curr.next
        prev.next=curr
    
    return head   


def reverseLL(head):
    prev=None
    curr=head

    while curr:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
    return prev


def mid(head):
    slower=head
    faster=head
    while faster !=None and faster.next !=None:
        slower=slower.next
        faster=faster.next.next
    return slower


def pallindrom(head):
    curr=head
    last=reverseLL(mid(head))

    if head ==None:
        return True
    while last !=None:
        if(curr.data != last.data):
            return False
        last=last.next
        curr=curr.next
    return True
    
def merge(head,last):
            h1 = head
            h2 = last
            while h2.next:
                temp=h1.next
                temp2=h2.next
                h1.next=h2
                h2.next=temp
                h1=temp
                h2=temp2
            return h1
def pairSum(head):
        curr=head
        tail=reverseLL(head)
        a=[]
        while tail:
            a.append(int(tail.val))
            curr=curr.next
            tail=tail.next
        return max(a)



head=inputLL()
# printLL(head)
# print(lengthLL(head))
# print('pallindrom')
# print(pallindrom(head))
# print("div 3")
# head=insertLL(head,0,123)
# printLL(head)
# head=insertLL(head,3,123)
# printLL(head)
# print("div 2")
# head=deleteLL(head,0)
# printLL(head)
# head=deleteLL(head,2)
# printLL(head)
# print("div 1")
# head=reverseLL(head)
# printLL(head)
# print("awesome")
# head=mid(head)
# printLL(head)
print(pairSum(head))



            



