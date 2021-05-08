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
    


# Creating a LinkedList 
ll = LinkedList()
ll.head = Node(4)
e2 = Node(5)
e3 = Node(1)
ll.head.next = e2
e2.next = e3

# insert
ll.insertFromHead('head') 
ll.insertFromTail('tail')
ll.insertAfter(e2,'after5')

head = ll.head

# remove
ll.remove(5)

ll.listprint()

