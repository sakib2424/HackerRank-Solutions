

    // Complete the removeDuplicates function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static SinglyLinkedListNode removeDuplicates(SinglyLinkedListNode head) {
        HashSet set = new HashSet();
        SinglyLinkedListNode prev = head;
        set.add(head.data);
        SinglyLinkedListNode pointer = head.next;
        while (pointer != null) {
            // System.out.println(pointer.data);
            if (set.contains(pointer.data)) {
                if (pointer.next != null) {
                    prev.next = pointer.next;
                    pointer = prev.next;
                }
                else {
                    prev.next = null;
                    return head;
                }
            }
            else {
                set.add(pointer.data);
                prev = pointer;
                pointer = pointer.next;
            }
        }
        return head;

    }


