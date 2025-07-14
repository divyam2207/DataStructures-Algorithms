# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        def foo(node):
            s = 0
            base = 0
            curr = node
            while curr:
                if base == 0:
                    s += 1 if curr.val == 1 else 0
                else:
                    s += (2**base) if curr.val == 1 else 0
                curr = curr.next
                base += 1
                print(s)
            return s 
        
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return foo(prev)
        
        
        
        
        