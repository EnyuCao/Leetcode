# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

idx = ListNode(3)
n = idx
n.next = ListNode(4)
n = n.next
n.next = ListNode(5)
n = n.next
print idx.val, idx.next.val
