

    // Complete the hasCycle function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static boolean hasCycle(SinglyLinkedListNode head) {
        if (head == null || head.next == null) {
            return false;
        }
        SinglyLinkedListNode slow = head;
        SinglyLinkedListNode fast = head.next;
        while (slow.next != null && fast.next != null && fast.next.next != null) {
            if (fast == slow) {
                return true;
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        return false;
    }


