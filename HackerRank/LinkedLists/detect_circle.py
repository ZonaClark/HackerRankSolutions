"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
	if head is None:
        return 0
    head.data = "visited"
    while head.next != None:
        if head.next.data == "visited":
            return 1
        head.next.data = "visited"
    return 0