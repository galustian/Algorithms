public class Main {
    public static void main(String[] args) {
        var numArray = new double[]{4, 6, 2, 344, 0, -1, 45};

        var sortedArray = TournamentSort.sort(numArray);

        for (var n: sortedArray) {
            System.out.println(n);
        }
    }
}
