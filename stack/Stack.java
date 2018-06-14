package stack;

public class Stack<Item> {
    private Node first = null;
    private int N = 0;

    public void push(Item item) {
        var second = first;
        N++;
        first = new Node(item, second);
    }

    public Item pop() {
        var item = first.item;
        first = first.next;
        N--;
        return item;
    }

    public int size() {
        return N;
    }

    private class Node {
        private Item item;
        private Node next;
        private Node(Item item, Node next) {
            this.item = item;
            this.next = next;
        }
    }
}