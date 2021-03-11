public class darkWilderness {
    public static void main(String[] args) {
        // 체스판에서 비숍과 쫄이 있다. 각 말의 위치는 string으로 받아지며,
        // 비숍의 이동범위안에 쫄이 있는지 확인해주고,
        // 있다면 True 없다면 false를 리턴한다.
    }

    // my
    boolean bishopAndPawn(String bishop, String pawn) {
        int bishopPosition = bishop.charAt(0) + bishop.charAt(1);
        int pawnPosition = pawn.charAt(0) + pawn.charAt(1);
        int test = 0, x = 2;

        if (bishopPosition == pawnPosition)
            return true;

        for (int i = 1; i < 8; i++) {
            x *= i;
            if (bishopPosition - x == pawnPosition) {
                if (bishop.charAt(0) - i == pawn.charAt(0) && bishop.charAt(1) - i == pawn.charAt(1))
                    return true;
            } else if (bishopPosition + x == pawnPosition) {
                if (bishop.charAt(0) + i == pawn.charAt(1)) {
                    if (bishop.charAt(1) - i == pawn.charAt(1) && bishop.charAt(1) + i == pawn.charAt(1)) {
                        return true;
                    }
                }
            }
            x = 2;
        }

        return false;
    }

    // elite
    boolean bishopAndPawn2(String bishop, String pawn) {
        return (Math.abs(bishop.charAt(0) - pawn.charAt(0))) == (Math.abs(bishop.charAt(1) - pawn.charAt(1)));
    }
}