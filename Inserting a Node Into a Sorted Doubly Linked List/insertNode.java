

    // Complete the sortedInsert function below.

    /*
     * For your reference:
     *
     * DoublyLinkedListNode {
     *     int data;
     *     DoublyLinkedListNode next;
     *     DoublyLinkedListNode prev;
     * }
     *
     */
    static DoublyLinkedListNode sortedInsert(DoublyLinkedListNode head, int data) {
        DoublyLinkedListNode pointer = head;
        if (data < head.data) {
            DoublyLinkedListNode insert = new DoublyLinkedListNode(data);
            insert.next = head;
            return insert;
        }
        while (pointer.next != null && data > pointer.next.data) {
            pointer = pointer.next;
        }
        DoublyLinkedListNode insert = new DoublyLinkedListNode(data);
        if (pointer.next != null) {
            insert.next = pointer.next;
        }
        pointer.next = insert;
        return head;
    }


