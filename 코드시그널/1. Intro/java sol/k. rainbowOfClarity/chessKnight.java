class RainbowOfClarity {
    public static void main(String[] args) {

    }

    // my
    int chessKnight(String cell) {
        int alpha = (int) cell.charAt(0);
        int num = Integer.parseInt(cell.substring(1));
        System.out.println(alpha);
        System.out.println(num);

        if (num < 7 && num > 2) {
            if (alpha < 103 && alpha > 98) {
                return 8;
            } else if (alpha == 98 || alpha == 103) {
                return 6;
            } else if (alpha == 97 || alpha == 104) {
                return 4;
            }
        } else if (num == 2 || num == 7) {
            if (alpha < 103 && alpha > 98) {
                return 6;
            } else if (alpha == 98 || alpha == 103) {
                return 4;
            } else if (alpha == 97 || alpha == 104) {
                return 3;
            }
        } else if (num == 1 || num == 8) {
            if (alpha < 103 && alpha > 98) {
                return 4;
            } else if (alpha == 98 || alpha == 103) {
                return 3;
            } else if (alpha == 97 || alpha == 104) {
                return 2;
            }
        }
        System.out.print("something else.....");
        return 0;
    }
    // elite

}