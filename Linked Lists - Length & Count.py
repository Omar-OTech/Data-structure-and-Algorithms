class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    count = 0
    while node:
        count += 1
        node = node.next
    return count

def count(node, data):
    count = 0
    while node:
        if node.data == data:
            count += 1
        node = node.next
    return count

def build_one_two_three():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    return one  

list = build_one_two_three()
print(length(None))       # 0, "Length of null list should be zero.")
print(length(Node(99)))   # 1, "Length of single node list should be one.")
print(length(list))       # 3, "Length of the three node list should be three.")
list = build_one_two_three();
print(count(list, 1))     # 1, "list should only contain one 1.")
print(count(list, 2))     # 1, "list should only contain one 2.")
print(count(list, 3))     # 1, "list should only contain one 3.")
print(count(list, 99))    # 0, "list should return zero for integer not found in list.")
print(count(None, 1))     # 0, "null list should always return count of zero.")