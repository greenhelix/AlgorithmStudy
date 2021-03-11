public class ExploringTheWaters {
    public static void main(String[] args) {
        /*
         * 입력값이 회문이 될수 있는지 판단해주는 알고리즘.
         */
    }

    boolean palindromeRearranging(String inputString) {
        int[] check = new int[26];
        int t = 0;
        int te = 0;

        for (int i = 0; i < inputString.length(); i++) {
            check[inputString.charAt(i) - 'a']++;
        }

        for (int i = 0; i < check.length; i++) {
            if (check[i] != 0)
                te++;
        }

        for (int i : check) {
            if (i % 2 == 1)
                t++;
        }
        return inputString.length() % 2 == t;
    }
}