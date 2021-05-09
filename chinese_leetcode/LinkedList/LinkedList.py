# A single node of a singly linked list
class Node:
  # constructor
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):  
        self.head = None
    
    # print linkedlist
    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next

    # insert from begining 
    def insertFromHead(self,newValue):
        newNode = Node(newValue)
        newNode.next = self.head
        self.head = newNode
    
    def insertFromTail(self,newValue):
        newNode = Node(newValue)
        newNode.next = None

        # find last node=> make node.next = newNode
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def insertAfter(self,target_node,newValue):
        # check target_node node exist 
        if target_node is None:
            return 

        newNode = Node(newValue)
        newNode.next = target_node.next
        target_node.next = newNode
    
    def remove(self,target_node_value):        
        # if the target_node is head 
        # find previous node, previous node.next = target_node.next
        head = self.head
        
        if target_node_value == head.data:
            print('1st node removed')
            self.head = head.next
            return 
        
        while (head is not None):
            if head.data == target_node_value:
                break
            prev = head
            head = head.next
        
        # handle nothing find
        if head is None:
            print('target not find')
            return 

        prev.next = head.next 

    def remove_from_last(self,n):

        dummy = Node(0,head)
# 1. use stack 
        stack = list()

# push all node into stack 
        cur = dummy 
        while cur:
            stack.append(cur)
            cur = cur.next
        
        for i in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
# 2. two pointer [0,1,2,3,4,5,6] => remove 5=> (first => 6), (sen => 4) 
# when first come to end, the second is the prev node of remove node
        first = head
        second = dummy 
        for i in range(n):
            first = first.next
        
        while first:
            first = first.next
            second = second.next 
        
        second.next = second.next.next

# return the head node (required)
        return dummy.next

    def reverseList(self):
        prev = None
        cur = self.head 

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

# need to set the haed 
        self.head = prev
        
    


# Creating a LinkedList 
ll = LinkedList()
ll.head = Node(4)
e2 = Node(5)
e3 = Node(1)
ll.head.next = e2
e2.next = e3

# insert
ll.insertFromHead('heads') 
ll.insertFromTail('tail')
ll.insertAfter(e2,'after5')

head = ll.head

# remove
# ll.remove(5)
# ll.remove_from_last(2)

# reverse 
ll.reverseList()

ll.listprint()