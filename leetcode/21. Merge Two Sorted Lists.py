# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next


# test code
def test_mergeTwoLists():
    solution = Solution()

    # Test case 1
    # List 1: 1 -> 2 -> 4
    # List 2: 1 -> 3 -> 4
    # Merged list: 1 -> 1 -> 2 -> 3 -> 4 -> 4
    list1 = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(4)
    list1.next = node1
    node1.next = node2

    list2 = ListNode(1)
    node3 = ListNode(3)
    node4 = ListNode(4)
    list2.next = node3
    node3.next = node4
    