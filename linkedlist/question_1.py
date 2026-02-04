class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a=Node(5)
b=Node(6)
c=Node(7)

a.next=b
b.next=c

head=a

# print linkedlist
def printLinkedList(head):
    curr = head
    while curr!=None:
        print(curr.data, end=" ")
        curr = curr.next
    
    print()

printLinkedList(head)


# insert new node beginning

newNode = Node(8)
newNode.next=head
head=newNode

printLinkedList(head)


# insert new node at end

newNode = Node(9)
curr = head
while curr.next!=None:
    curr=curr.next
curr.next=newNode
printLinkedList(head)


# insert at the middle
k=3
newNode = Node(10)
curr=head
for i in range(k-1):
    curr=curr.next
newNode.next=curr.next
curr.next=newNode
printLinkedList(head)


# delete at the beginning
head=head.next
printLinkedList(head)


# delete at the end
curr=head
while curr.next.next!=None:
    curr=curr.next
curr.next=None
printLinkedList(head)


# delete at the mid/kth node
k=2
curr=head
for i in range(k-1):
    curr=curr.next
curr.next=curr.next.next
printLinkedList(head)