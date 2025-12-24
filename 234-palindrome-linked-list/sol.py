# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false
 
# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        reversedMiddle = self.reverse(slow)
        
        while reversedMiddle:
            if head.val != reversedMiddle.val:
                return False
            
            head = head.next
            reversedMiddle = reversedMiddle.next
            
        return True

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        temp = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
            
            
        