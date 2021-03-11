public class RainsOfReason {
    public static void main(String[] args) {
        /*
         * 체스판이 있다. 각 위치는 true false로 번갈아가며 들어가 있어 체스판같이 색이 있는 칸과 없는 칸으로 구분된다. 어떠한 좌표
         * 두곳을 입력했을 때, 그 좌표들이 서로 같은 상태로 되어있다면 true 아니라면 false 이다.
         */
    }

    boolean chessBoardCellColor(String cell1, String cell2) {
        char hor1 = cell1.charAt(0);
        String ver1 = cell1.substring(1);
        int hori1 = (int) hor1;
        int vert1 = Integer.parseInt(ver1);

        char hor2 = cell2.charAt(0);
        String ver2 = cell2.substring(1);
        int hori2 = (int) hor2;
        int vert2 = Integer.parseInt(ver2);

        String[][] chess = new String[8][8];

        for (int i = 0; i < chess.length; i++) {

            for (int j = 0; j < chess[0].length; j++) {

                if (i % 2 == 0) {

                    if (j % 2 == 0) {
                        chess[i][j] = "ON";
                    } else {
                        chess[i][j] = "OFF";
                    }

                } else {

                    if (j % 2 == 0) {
                        chess[i][j] = "OFF";
                    } else {
                        chess[i][j] = "ON";
                    }
                }
            }
        }
        int[][] cell = { { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' }, { 1, 2, 3, 4, 5, 6, 7, 8, } };
        boolean result = true;
        String result1 = "", result2 = "";

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (hori1 + vert1 == cell[0][i] + cell[1][j]) {
                    result1 = chess[i][j];
                }
            }
        }
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (hori2 + vert2 == cell[0][i] + cell[1][j]) {
                    result2 = chess[i][j];
                }
            }
        }
        return result = result1 == result2 ? true : false;
    }
}