# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


# Test cases
def test_reorderList():
    solution = Solution()


    # Test case 1
    # List: 1 -> 2 -> 3 -> 4
    # Reordered list: 1 -> 4 -> 2 -> 3
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    solution.reorderList(head)
    assert head.val == 1
    assert head.next.val == 4
    assert head.next.next.val == 2
    assert head.next.next.next.val == 3
    assert head.next.next.next.next == None
    
    # Test case 2
    # List: 1 -> 2 -> 3 -> 4 -> 5
    # Reordered list: 1 -> 5 -> 2 -> 4 -> 3
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    solution.reorderList(head)
    assert head.val == 1
    assert head.next.val == 5
    assert head.next.next.val == 2
    assert head.next.next.next.val == 4

