public class Main {
    public static void main(String[] args) {
        var numArray = new double[]{4, 6, -1, 44, 34, 4, 2345, 4, 43, 77, 3, 0, 0};

        var sortedArray = TournamentSort.sort(numArray);

        for (var n: sortedArray) {
            System.out.println(n);
        }
    }
}
