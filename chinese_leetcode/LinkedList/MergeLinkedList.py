class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next



def merge(l1,l2):
    prevhead = ListNode(0)
    # moving pointer
    prev = prevhead

    # pointer next to node with min(val)
    while l1 and l2:
        if l1.val > l2.val:
            prev.next = l2
            l2 = l2.next
        else:
            prev.next = l1
            l1 = l1.next

    # pre define handle the rest 
    prev = prev.next

    if l1:
        prev.next = l1
    else:
        prev.next = l2
    
    return prevhead.next


     