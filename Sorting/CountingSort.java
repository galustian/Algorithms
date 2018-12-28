public class CountingSort {
    public static void main(String[] args) {
        int[] arr = {1, 2, 54, 34, 3, -456, 4, -32};
        int[] sorted = sort(arr, 54, -456);
        for (int i = 0; i < sorted.length; i++) {
            System.out.print(sorted[i] + " ");
        }
    }

    public static int[] sort(int[] arr, int max, int min) {
        assert max >= min : "max is smaller than min...";
        
        int[] counter = new int[Math.abs(max) + Math.abs(min) + 1];
        for (int i = 0; i < arr.length; i++) {
            counter[arr[i] + Math.abs(min)]++;
        }

        int[] sorted = new int[arr.length];
        int idx = 0;
        for (int i = 0; i < counter.length; i++) {
            for (int j = 0; j < counter[i]; j++) {
                sorted[idx] = i - Math.abs(min);
                idx++;
            }
        }
        return sorted;
    }

}