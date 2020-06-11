

	/* 
    
    class Node 
    	int data;
    	Node left;
    	Node right;
	*/
	public static void levelOrder(Node root) {
        if (root == null) {
            return;
        }
        List<List<Node>> list = new ArrayList<>();
        list.add(new ArrayList<Node>());
        list.get(0).add(root);
        int counter = 0;
        while (list.get(counter).size() != 0) {
            list.add(new ArrayList());
            for (Node x: list.get(counter)) {
                if (x.left != null) {
                    list.get(counter + 1).add(x.left);
                }
                if (x.right != null) {
                    list.get(counter + 1).add(x.right);
                }
            }
            // for (int i = 0; i < list.get(counter).size(); i++) {
            //     if (list.get(counter).get(i) != null) {
            //         list.get(counter+ 1).add(x.left);
            //     }
            //     if (x.right != null) {
            //         list.get(counter).add(x.right);
            //     }
            // }
            counter++;
        }
        // for (List level: list) {
        //     for (Node x: level) {
        //         System.out.print(x.data + " ");
        //     }
        // }
        for (int i = 0; i < list.size(); i++) {
            for (int j = 0; j < list.get(i).size(); j++) {
                System.out.print(list.get(i).get(j).data + " ");
            }
        }
    }


