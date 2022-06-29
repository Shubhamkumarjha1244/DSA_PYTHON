


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def inputLL():
    inputlist=[int(ele) for ele in input("enter number--> ").split()]
    head=None
    tail=None
    for currdata in inputlist:

        if currdata == -1:
            break
        newnode=Node(currdata)

        if head is None:
            head =newnode 
            tail=newnode
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
        c+=1
        head=head.next
    return count
def insertLL(head,pos,data):
    if pos <0 and pos> lengthLL(head):
        return head
    
    nodenew=Node(data)
    curr=head
    prev=None
    count=0    
    while count<pos: #zero pe loop nahi chalega
        prev=curr
        curr=curr.next
        count +=1
    if prev is None:
            head=nodenew
            nodenew.next=curr
    else:
            prev.next=nodenew
            nodenew.next=curr
    return head

def deleteLL(head,pos):
    if pos <0 and pos> lengthLL(head):
        return head
    curr=head
    prev=None
    count=0    
    while count<pos: #zero pe loop nahi chalega
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


head=inputLL()
printLL(head)
print("\n insert node")
head=insertLL(head,2,3) 
print('\n')      
printLL(head)
head=insertLL(head,0,3) 
print('\n')      
printLL(head)
head=insertLL(head,7,7) 
print('\n')      
printLL(head)
print("\n delete node")
head=deleteLL(head,0)
print('\n')
printLL(head)
head=deleteLL(head,4)
print('\n')
printLL(head)


