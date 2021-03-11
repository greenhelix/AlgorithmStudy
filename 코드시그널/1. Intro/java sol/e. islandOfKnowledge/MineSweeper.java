public class IslandOfKnowledge {
    public static void main(String[] args) {
        /*
         * 지뢰찾기 게임.. false 위치가 지뢰가 될수 있는 위치라고 하면. 그 위치 주변은 true이다. 그렇다면, 그 true의 위치는 1
         * 이되거나 주변 False의 갯수에 따라 측정되게 만들어라.
         */

    }

    // my
    int[][] minesweeper(boolean[][] matrix) {
        int[][] check = new int[matrix.length][];

        for (int a = 0; a < matrix.length; a++) {
            check[a] = new int[matrix[0].length];

            for (int b = 0; b < matrix[0].length; b++) {

                for (int x = a - 1; x <= a + 1; x++) {

                    for (int y = b - 1; y <= b + 1; y++) {
                        if (x == a && y == b)
                            continue;
                        else {
                            try {
                                if (matrix[x][y])
                                    check[a][b] += 1;
                            } catch (Exception ex) {

                            }
                        }
                    }
                }
            }
        }
        return check;
    }
}