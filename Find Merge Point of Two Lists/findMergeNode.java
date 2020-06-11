

    // Complete the findMergeNode function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static int findMergeNode(SinglyLinkedListNode head1, SinglyLinkedListNode head2) {
        HashSet set = new HashSet();
        SinglyLinkedListNode pointer = head1;
        SinglyLinkedListNode pointer2 = head2;
        while (pointer != null) {
            set.add(pointer);
            pointer = pointer.next;
        }
        while (pointer2 != null) {
            if (set.contains(pointer2)) {
                return pointer2.data;
            }
            pointer2 = pointer2.next;
        }
        return -1;
    }


