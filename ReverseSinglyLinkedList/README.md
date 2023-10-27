# [Leetcode Problem 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## Thought Process

    The reverseList function is defined, which takes the head of a singly-linked list as an argument. It is designed to reverse the linked list and return the new head of the reversed list.

    The function first checks for two edge cases:
        If the input head is null (meaning an empty list) or if the head.next is null (meaning a list with only one node), it returns the head as there is nothing to reverse in these cases.

    For other cases, it recursively calls the reverseList function on the next node, effectively reversing the tail of the list.

    Once the recursive calls have reversed the rest of the list, the code performs the actual reversal of the head and the next nodes:
        It sets the next of the current head to be the next node's next, effectively reversing the connection to the next node.
        Then, it sets the next of the current head to null, breaking the original connection.

    Finally, it returns the new head of the reversed list, which was originally the tail of the original list.

Essentially, the code recursively reverses the linked list by reversing the connections between nodes and then returns the new head of the reversed list.
