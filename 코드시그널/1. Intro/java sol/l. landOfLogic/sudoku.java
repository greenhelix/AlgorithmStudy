class LandOfLogic {
    public static void main(String[] args) {

    }

    // my
    boolean sudoku(int[][] grid) {
        int[] result = new int[3];
        int[] set = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        for (int i = 0; i < 9; i++) {
            if (contain(grid[i], set) == false) {
                System.out.println("1~9 NOT");
                return false;
            }
        }
        // column check(세로) row check(가로)
        for (int i = 0; i < 9; i++) {
            int colSum = 0;
            int rowSum = 0;
            for (int j = 0; j < 9; j++) {
                colSum += grid[i][j];
                result[0] = colSum == 45 ? 1 : 0;
                rowSum += grid[j][i];
                result[1] = rowSum == 45 ? 1 : 0;
            }
            if (result[0] == 0) {
                System.out.println("col error");
                return false;
            }
            if (result[1] == 0) {
                System.out.println("row error");
                return false;
            }
        }
        // square check
        if (result[0] == 1 && result[1] == 1) {
            for (int sq = 0; sq < 3; sq++) {
                int range = 3;
                int sqSum = 0;
                int rowSP = 0;
                int colSP = 0;
                // column 3 square logic
                for (int sqRow = 1; sqRow < 4; sqRow++) {
                    for (int r = rowSP; r < sqRow * 3; r++) {
                        for (int c = colSP; c < range; c++) {
                            sqSum += grid[r][c];
                        }
                    }
                    result[2] = sqSum == 45 ? 1 : 0;
                    if (result[2] == 0) {
                        System.out.println("sq error");
                        return false;
                    }
                    rowSP += 3;
                    sqSum = 0;
                }
                rowSP = 0;
                colSP += 3;
            }
        }
        System.out.println(">>" + Arrays.toString(result) + " sum is 3?:" + Arrays.stream(result).sum());
        return Arrays.stream(result).sum() == 3 ? true : false;
    }

    // 숫자 다있는지 확인 1-9까지 메서드 생성함...
    public static boolean contain(int[] array, int[] num) {
        int[] count = new int[9];
        for (int i = 0; i < 9; i++) {
            for (int j : array) {
                if (num[i] == j) {
                    count[i] = 1;
                    break;
                }
            }
        }
        System.out.println(Arrays.toString(count));

        return Arrays.stream(count).sum() == 9 ? true : false;
    }

    // elite
    boolean elitesudoku(int[][] grid) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                int[][] counts = new int[3][9];
                for (int x = 0; x < 3; x++) {
                    for (int y = 0; y < 3; y++) {
                        counts[0][grid[i * 3 + x][j * 3 + y] - 1] = 1;
                        counts[1][grid[i * 3 + j][x * 3 + y] - 1] = 1;
                        counts[2][grid[x * 3 + y][i * 3 + j] - 1] = 1;
                    }
                }
                for (int k = 0; k < 9; k++) {
                    if (counts[0][k] == 0 || counts[1][k] == 0 || counts[2][k] == 0) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

}