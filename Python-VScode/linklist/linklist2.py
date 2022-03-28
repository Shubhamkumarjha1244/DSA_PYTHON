class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def inputLL():
    inputlist= [int(ele) for ele in input('Enter value').split()]
    head=None
    tail=None

    for curr in inputlist:
        if curr == -1:
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

def midofLL(head):
    fast=head
    slow=head

    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    return slow

def reverseLL(head):
    curr=head
    prev=None
    while curr:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
    return prev

def pallindrom(head):
    if head is None:
        return True
    first=head
    last=reverseLL(midofLL(head).next)
    

    while last:
        if first.data != last.data:
            return False
        last=last.next
        first=first.next
    return True 

head=inputLL()
printLL(head)
print(pallindrom(head))
