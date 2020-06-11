

    // Complete the compareLists function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static boolean compareLists(SinglyLinkedListNode head1, SinglyLinkedListNode head2) {
        if (head1 == null) {
            if (head2 == null) {
                return true;
            }
            return false;
        }
        if (head2 == null) {
            if (head1 == null) {
                return true;
            }
            return false;
        }
        SinglyLinkedListNode pointer = head1;
        SinglyLinkedListNode pointer2 = head2;
        while (pointer != null) {
            if (pointer2 == null) {
                return false;
            }
            if (pointer.data != pointer2.data) {
                return false;
            }
            pointer = pointer.next;
            pointer2 = pointer2.next;
        }
        return true;
    }


