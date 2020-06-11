

# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):
    if (head == None):
        return
    store = []
    store.append(head.data)
    pointer = head.next
    while (pointer):
        store.insert(0,pointer.data)
        pointer = pointer.next
    for data in store:
        print(str(data))


