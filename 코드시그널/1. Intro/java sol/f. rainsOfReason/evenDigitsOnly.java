public class RainsOfReason {
    public static void main(String[] args) {
        /*
         * 입력되는 숫자의 한자리 자리마다 다 짝수가 들어가 있는지 확인하는 알고리즘이다.
         */
    }

    boolean evenDigitsOnly(int n) {
        int length2 = (int) (Math.log10(n) + 1);
        boolean result = true;
        int next = 0;

        for (int i = 1; i <= length2; i++) {
            next = n % 10;
            n /= 10;

            if (next % 2 == 0) {
                continue;
            } else if (next % 2 != 0) {
                return result = false;
            }
        }
        return result;
    }

}