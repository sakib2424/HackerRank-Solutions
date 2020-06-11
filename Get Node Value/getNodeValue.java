

    // Complete the getNode function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static int getNode(SinglyLinkedListNode head, int positionFromTail) {
        SinglyLinkedListNode pointer = head;
        SinglyLinkedListNode pointer2 = head;
        for (int i = 0; i < positionFromTail; i++) {
            pointer2 = pointer2.next;
        }
        while (pointer2.next != null) {
            pointer = pointer.next;
            pointer2 = pointer2.next;
        }
        return (pointer.data);


    }


