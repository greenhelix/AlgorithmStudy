class LandOfLogic {
    public static void main(String[] args) {

    }

    // my
    int differentSquares(int[][] matrix) {

        Set<String> squaresSet = new HashSet<String>();

        for (int i = 0; i < matrix.length - 1; i++) {
            for (int j = 0; j < matrix[0].length - 1; j++) {
                squaresSet.add(String.format("%d%d%d%d", matrix[i][j], matrix[i][j + 1], matrix[i + 1][j],
                        matrix[i + 1][j + 1]));
            }
        }
        return squaresSet.size();
    }

    // elite
    int elitedifferentSquares(int[][] matrix) {
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < matrix.length - 1; i++) {
            for (int j = 0; j < matrix[0].length - 1; j++) {
                String temp = String.valueOf(matrix[i][j]) + ";" + String.valueOf(matrix[i + 1][j]) + ";"
                        + String.valueOf(matrix[i][j + 1]) + ";" + String.valueOf(matrix[i + 1][j + 1]);
                set.add(temp);
            }
        }
        return set.size();
    }

}