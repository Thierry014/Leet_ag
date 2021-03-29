class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

    def deleteDuplicates(head):
    # ! set up a point to modify listnode operations
        cur = head 
    
        while cur and cur.next:
            if cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
           
        return head


    def mergeTwoLists(l1, l2):
        dummy = temp = ListNode(0)
        
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
            # print(temp)
            print(dummy)
    

        temp.next = l1 or l2 
        return dummy.next