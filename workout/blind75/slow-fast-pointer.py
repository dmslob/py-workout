# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that
# can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
# https://leetcode.com/problems/linked-list-cycle/?envType=problem-list-v2&envId=oizxjoit

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def has_cycle(head):
    if not head:
        return False
    slow = head
    fast = head.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


def find_middle(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

print(has_cycle(head))  # Output: True
