class Node:
    def __init__(self,data):
        self.next=None
        self.data=data


def inputLL():
    inputlist=[int(ele) for ele in input("Enter value for linklist").split()]
    head=None
    tail=None
    for curr in inputlist:
        if curr ==-1:
            break
       
        newnode=Node(curr)

        if head is None:
            head=newnode
            tail=head
        else:
            tail.next=newnode
            tail=newnode

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
    if pos<0 or pos>lengthLL(head):
        return head
    
    prev=None
    curr=head
    count=0

    while count < pos:
        prev=curr
        curr=curr.next
        count+=1
    newnode=Node(data)
    if prev is None:
        head=newnode
        newnode.next=curr
    else:
        prev.next=newnode
        newnode.next=curr
    return head

def deleteLL(head,pos):
    if pos<0 or pos>lengthLL(head):
        return head
    prev=None
    curr=head
    count=0

    while count < pos :
        prev=curr
        curr=curr.next
        count +=1

    if prev is None:
                head=curr.next
    else:
        curr=curr.next
        prev.next=curr

    return head










head=inputLL()

printLL(head)
head=insertLL(head,0,11)
printLL(head)
head=insertLL(head,5,69)
printLL(head)
head=insertLL(head,7,80)
printLL(head)
print('delete operation ')
head=deleteLL(head,0)
printLL(head)
head=deleteLL(head,6)
printLL(head)
head=deleteLL(head,3)
printLL(head)

