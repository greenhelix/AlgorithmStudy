public class ThroughTheFog {
    public static void main(String[] args) {
        /*
         * 주어진 문자배열을 경우의 수대로 봤을때, 연속되는 문자열로 되는지 확인하라. 단 한 문자만 바뀌면 성립되면 true로 허용한다.
         */
    }

    boolean stringsRearrangement(String[] input) {
        boolean[] used = new boolean[input.length];

        findSequence(input, null, used, 0);
        return success;
    }

    boolean success = false;

    void findSequence(String[] a, String prev, boolean[] used, int n) {
        if (n == a.length) {
            success = true;
            return;
        }
        for (int i = 0; i < a.length; i++) {
            if (!used[i] && (prev == null || differByOne(prev, a[i]))) {
                used[i] = true;
                findSequence(a, a[i], used, n + 1);
                used[i] = false;
            }
        }
    }

    boolean differByOne(String a, String b) {
        int count = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                count++;
            }
        }
        return count == 1;
    }

}