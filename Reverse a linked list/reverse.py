

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    if (not head or not head.next):
        return head
    prev = head
    pointer = prev.next
    pointer2 = pointer.next
    head.next = None
    while (pointer):
        print(pointer.data)
        pointer.next = prev
        prev = pointer
        pointer = pointer2
        if (pointer):
            pointer2 = pointer.next
    return prev


