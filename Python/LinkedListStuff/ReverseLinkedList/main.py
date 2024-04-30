# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base case check
        if not head or not head.next:
            return head
        # recursively calling the reverseList using head.next to move through list until the end
        reversed_head =  self.reverseList(head.next)
        # reverse the pointers once the recursion unwinds and we are coming back this will reverse the pointers
        head.next.next = head
        # THIS IS NECESSARY to prevent the original ist from forming a cycle after reversal
        head.next = None
        # our output we need
        return reversed_head
