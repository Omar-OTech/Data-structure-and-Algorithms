# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        




# Test cases
def test_hasCycle():
    solution = Solution()

    # Test case 1: Linked list with a cycle
    # List: 3 -> 2 -> 0 -> -4 -> (cycle back to node 2)
    head = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(0)
    node3 = ListNode(-4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1  # Creates a cycle back to node1 (2)
    
    assert solution.hasCycle(head) == True, "Test case 1 failed"

    # Test case 2: Linked list with a cycle
    # List: 1 -> 2 -> (cycle back to node 1)
    head = ListNode(1)
    node1 = ListNode(2)
    head.next = node1
    node1.next = head  # Creates a cycle back to head (1)
    
    assert solution.hasCycle(head) == True, "Test case 2 failed"

    # Test case 3: Linked list without a cycle
    # List: 1 -> 2 -> 3 -> None
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    head.next = node1
    node1.next = node2
    
    assert solution.hasCycle(head) == False, "Test case 3 failed"

    # Test case 4: Single node with no cycle
    # List: 1 -> None
    head = ListNode(1)
    
    assert solution.hasCycle(head) == False, "Test case 4 failed"

    # Test case 5: Empty list (None)
    head = None
    
    assert solution.hasCycle(head) == False, "Test case 5 failed"

    print("All test cases passed!")

# Run the tests
test_hasCycle()

