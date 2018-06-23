public class BitStream {
    private byte[] bytes;
    private int buffer;

    private int N = 0; // current byte
    private int n = 7; // current bit in byte

    private final int EOF = -1;

    public BitStream(byte[] bytes) {
        this.bytes = bytes;
        buffer = bytes[0] & 0xff;
    }

    public boolean isEmpty() {
        return buffer == EOF;
    }

    private void fillBuffer() {
        try {
            n = 7;
            buffer = bytes[++N] & 0xff;
        } catch (IndexOutOfBoundsException e) {
            buffer = EOF;
        }
    }

    public boolean readBoolean() {
        boolean bit = ((buffer >> n) & 1) == 1;
        n--;
        if (n == -1) fillBuffer();
        return bit;
    }
}
