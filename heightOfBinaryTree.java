

	/*
    class Node 
    	int data;
    	Node left;
    	Node right;
	*/
	public static int height(Node root) {
        if(root.left == null) {
            if (root.right == null) {
                return 0;
            }
            return height(root.right) + 1;
        }
        else {
            if (root.right == null) {
                return height(root.left) + 1;
            }
        }
        return Math.max(height(root.left), height(root.right)) + 1;
    }


