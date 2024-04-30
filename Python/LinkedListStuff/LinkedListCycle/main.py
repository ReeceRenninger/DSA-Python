# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # create a container (set) to add each node into
        loop = set()
        # while head is valid, if our head is in our container, return True
        while(head):
            if(head in loop):
                return True
            # if we make it out of container check, we add the head to our container
            loop.add(head)
            # head moves to head.next at end of each while loop to move through the LL
            head = head.next
        # if we make it through the whole LL without finding the head again, return False
        return False
            