final class TournamentSort {

    private static boolean leftEmpty(Node node) {
        return node.left == null || node.left.empty;
    }
    private static boolean rightEmpty(Node node) {
        return node.right == null || node.right.empty;
    }

    private static double popTreeWinner(Node node) {
        double bestValue = node.value;
        node.empty = true;

        setNewWinnerAfterPop(node);

        return bestValue;
    }

    private static void setNewWinnerAfterPop(Node node) {
        if (!leftEmpty(node) && !rightEmpty(node)) {
            node.empty = false;

            if (node.left.value < node.right.value) {
                node.value = node.left.value;
                node.left.empty = true;
                setNewWinnerAfterPop(node.left);
            } else {
                node.value = node.right.value;
                node.right.empty = true;
                setNewWinnerAfterPop(node.right);
            }
        } else if (!leftEmpty(node) && rightEmpty(node)) {
            node.value = node.left.value;
            node.left.empty = true;
            node.empty = false;
            setNewWinnerAfterPop(node.left);
        } else if (leftEmpty(node) && !rightEmpty(node)) {
            node.value = node.right.value;
            node.right.empty = true;
            node.empty = false;
            setNewWinnerAfterPop(node.right);
        }
    }

    private static Node[] extendOddNodes(Node[] nodes) {
        var tempNodes = new Node[nodes.length + 1];
        
        for (int i = 0; i < nodes.length; i++) {
            tempNodes[i] = nodes[i];
        }
        
        tempNodes[tempNodes.length-1] = new Node();
        tempNodes[tempNodes.length-1].empty = true;
        
        return tempNodes;
    }

    // Number of Nodes is always even
    private static Node createTree(Node[] nodes) {
        if (nodes.length % 2 == 1) {
            nodes = extendOddNodes(nodes);
        }

        assert nodes.length % 2 == 0;
        
        var winnerNodes = new Node[nodes.length / 2];

        for (int i = 0; i < nodes.length / 2; i++) {
            winnerNodes[i] = new Node();

            winnerNodes[i].left = nodes[i*2];
            winnerNodes[i].right = nodes[i*2+1];

            // catch empty node (correction for odd number of sorting elements)
            if (i == winnerNodes.length-1 && rightEmpty(winnerNodes[i])) {
                winnerNodes[i].value = winnerNodes[i].left.value;
                winnerNodes[i].left.empty = true;
                setNewWinnerAfterPop(winnerNodes[i].left);
                break;
            }

            if (winnerNodes[i].left.value < winnerNodes[i].right.value) {
                winnerNodes[i].value = winnerNodes[i].left.value;
                winnerNodes[i].left.empty = true;
                setNewWinnerAfterPop(winnerNodes[i].left);
            } else {
                winnerNodes[i].value = winnerNodes[i].right.value;
                winnerNodes[i].right.empty = true;
                setNewWinnerAfterPop(winnerNodes[i].right);
            }
        }

        if (winnerNodes.length == 1) {
            return winnerNodes[0];
        }

        return createTree(winnerNodes);
    }

    static double[] sort(double[] sortArray) {
        // if sortArray length is odd, add extra node (to easily construct tournament-tree)
        var nodes = new Node[sortArray.length + sortArray.length % 2];

        for (int i = 0; i < sortArray.length; i++) {
            nodes[i] = new Node(sortArray[i]);
        }

        // assert nodes[sortArray.length-1].empty || sortArray.length % 2 == 0;

        var tree = createTree(nodes);

        assert sortArray.length < 3 || tree.value >= tree.left.value && tree.value >= tree.right.value;

        var sorted = new double[sortArray.length];
        for (int i = 0; i < sortArray.length; i++) {
            sorted[i] = popTreeWinner(tree);
        }

        return sorted;
    }
}

class Node {
    double value;
    boolean empty;
    Node left;
    Node right;
    Node(){}
    Node(double value) { this.value = value; }
}