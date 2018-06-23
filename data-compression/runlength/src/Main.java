public class Main {
    public static void main(String[] args) {
        byte[] bytes = new byte[]{(byte)255, 0, 0, 0, 0, 0, (byte)255};

        byte[] encoded = RunLength.encode(bytes);
        System.out.println("Encoded: ");
        for (var b: encoded) {
            System.out.print(b + ", ");
        }

        byte[] decoded = RunLength.decode(encoded);
        System.out.println("\nDecoded: ");
        for (var b: decoded) {
            System.out.print((b & 0xff) + ", ");
        }
    }
}