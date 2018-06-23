import java.util.ArrayList;

public final class RunLength {
    public static byte[] encode(byte[] bytes) {
        var bitStream = new BitStream(bytes);
        var byteArrayList = new ArrayList<Byte>();

        boolean currentBit = false;
        byte bitCounts = 0;

        while (!bitStream.isEmpty()) {
            if (bitCounts == (byte)255) {
                byteArrayList.add(bitCounts);
                bitCounts = 0;
            }

            boolean bit = bitStream.readBoolean();

            if (bit == currentBit) {
                bitCounts++;
            } else {
                byteArrayList.add(bitCounts);

                currentBit = !currentBit;
                bitCounts = 1;
            }
        }
        byteArrayList.add(bitCounts);

        // put encoded bytes to byte[] array
        byte[] encodedBytes = new byte[byteArrayList.size()];
        for (int i = 0; i < byteArrayList.size(); i++) {
            encodedBytes[i] = byteArrayList.get(i);
        }

        return encodedBytes;
    }

    public static byte[] decode(byte[] bytes) throws IllegalArgumentException {
        boolean currentBit = false;
        var bitString = new StringBuilder();

        for (byte b: bytes) {
            int bitNum = b & 0xff;
            if (currentBit) {
                bitString.append(new String(new char[bitNum]).replace('\0', '1'));
            } else {
                bitString.append(new String(new char[bitNum]).replace('\0', '0'));
            }
            currentBit = !currentBit;
        }

        if (bitString.length() % 8 != 0) {
            throw new IllegalArgumentException("corrupt encoding");
        }

        byte[] decodedBytes = new byte[bitString.length() / 8];

        for (int i = 0; i <= bitString.length()-8; i += 8) {
            var subString = bitString.substring(i, i+8);
            var b = Integer.parseInt(subString, 2);
            decodedBytes[i / 8] = (byte) b;
        }

        return decodedBytes;
    }
}
