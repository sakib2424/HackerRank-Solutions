

    // Complete the reverse function below.

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
    static DoublyLinkedListNode reverse(DoublyLinkedListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        DoublyLinkedListNode p = head;
        DoublyLinkedListNode p1 = head.next;
        DoublyLinkedListNode p2 = p1.next;
        p.next = null;
        p.prev = p1;
        while (p1 != null) {
            p1.next = p;
            p1.prev = p2;
            p = p1;
            p1 = p2;
            if (p2 != null){
                p2 = p2.next;
            }
        }
        return p;

    }


