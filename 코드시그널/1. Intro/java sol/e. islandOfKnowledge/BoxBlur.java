public class IslandOfKnowledge {
    public static void main(String[] args) {
        /*
         * 박스블러. 어떠한 이미지를 불러 처리할때, 적용되는 알고리즘. 화질을 블러 처리하는 방법은 알정하게 분배되어있는 이미지의 픽셀들을 동일한
         * 비례값으로 떨어트리는 것이다.
         */

    }

    // my
    int[][] boxBlur(int[][] image) {
        int x = image[0].length - 2;
        int y = image.length - 2;
        int[][] b = new int[y][];

        for (int i = 0; i < y; i++) {
            b[i] = new int[x];
            for (int j = 0; j < x; j++) {
                b[i][j] = image[i][j] + image[i][j + 1] + image[i][j + 2] + imgae[i + 1][j] + image[i + 1][j + 1]
                        + image[i + 1][j + 2] + image[i + 2][j] + image[i + 2][j + 1] + image[i + 2][j + 2];
                b[i][j] /= 9;
            }
        }
        return b;
    }
}