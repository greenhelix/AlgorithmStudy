public class DivingDeeper {
    public static void main(String[] args) {
        /**
         * 주어진 문자에서 알파벳의 종류의 수를 리턴하는 알고리즘이다.
         */
    }

    int differentSymbolsNaive(String s) {
        int[] check = new int[26];
        int result = 0;

        for (int i = 0; i < s.length(); i++) {
            check[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < check.length; i++) {
            if (check[i] != 0)
                result++;
        }
        return result;
    }
}