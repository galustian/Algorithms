import stack.Stack;

public class StackDemo {
    public static void main(String[] args) {
        var stack = new Stack<Integer>();
        stack.push(45);
        stack.push(444);
        stack.push(4444);
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        stack.push(69);
        stack.push(88);
        stack.push(111);
        System.out.println(stack.size());
    }
}