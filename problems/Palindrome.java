import java.util.Stack;

public class Palindrome {
    public static void main(String[] args) {
        var str = args[0];
        var charArray = str.toCharArray();

        var stack = new Stack<Character>();
        for (var c: charArray) {
            stack.push(c);
        }

        var reverseStr = "";
        while (stack.size() != 0) {
            reverseStr += stack.pop();
        }
        
        if (reverseStr.equals(str)) {
            System.out.println("Is a Palindrome!");
        } else {
            System.out.println("Not a Palindrome.");
        }
    }
}