/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  if( head === null || head.next === null){
      return head; // edge case catcher
  }
  // call the function recursively
  let reverse = reverseList(head.next)
  // set our head to next next 
  head.next.next = head;
  // need our null
  head.next = null;
  return reverse;
};