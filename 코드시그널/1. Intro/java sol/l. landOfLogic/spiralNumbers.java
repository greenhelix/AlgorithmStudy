class LandOfLogic {
    public static void main(String[] args) {

    }

    // my
    int[][] spiralNumbers(int n) {
        int[][] bucket = new int[n][n];
        int range = n;
        int start = 0;
        for (int h = 0; h < n; h++) {
            // 1stream
            int right = 1;
            for (int i = start; i < range; i++) {
                if (start != 0) {
                    bucket[start][i] = bucket[start][i - 1] + right;
                }
                if (start == 0) {
                    bucket[start][i] = bucket[i][start] + right;
                    right++;
                }
            }
            // 2stream
            int down = 1;
            for (int j = start + 1; j < range; j++) {
                bucket[j][range - 1] = bucket[j - 1][range - 1] + down;
            }
            // 3stream
            for (int x = range - 2; x >= start; x--) {
                bucket[range - 1][x] = bucket[range - 1][x + 1] + 1;
            }
            // 4stream
            for (int z = range - 2; z > start; z--) {
                bucket[z][start] = bucket[z + 1][start] + 1;
            }
            range -= 1;
            start += 1;
        }
        return bucket;
    }

    // elite
    int[][] elitespiralNumbers(int n) {
        int[][] array = new int[n][n];

        int left = 0;
        int right = n - 1;
        int top = 0;
        int down = n - 1;

        for (int counter = 1; counter <= n * n;) {
            for (int x = left; x <= right; x++)
                array[top][x] = counter++;
            top++;

            for (int y = top; y <= down; y++)
                array[y][right] = counter++;
            right--;

            for (int x = right; x >= left; x--)
                array[down][x] = counter++;
            down--;

            for (int y = down; y >= top; y--)
                array[y][left] = counter++;
            left++;
        }

        return array;
    }
}