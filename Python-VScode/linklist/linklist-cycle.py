from tracemalloc import start


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def inputLL():
    inputlist=[int(ele) for ele in input().split()]
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

def makeCycle(head):
    if head is None:
        return
    slow=head
    fast=head
    prev=None
    while fast and fast.next :

        slow=slow.next
        prev=fast.next
        fast=fast.next.next
    if fast==None:
        prev.next=slow.next
    else:
        fast.next=slow.next
    return head
    
def detectCycle(head):
    slow=head
    fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow == fast:
            
            return slow
    return None

def detectstartingofcycle(head):
    meet=detectCycle(head)
    start=head
    while start != meet:
        start=start.next
        meet=meet.next
    return meet

def removecycle(head):
    curr=detectCycle(head)
    prev=None
    while curr != detectstartingofcycle(head):
        prev=curr
        curr=curr.next
    if prev is None :
        return prev
    else:
        prev.next =None
    return head

        

head=inputLL()
printLL(head)
head=makeCycle(head)
print("Cycle removed")
printLL(removecycle(head))

