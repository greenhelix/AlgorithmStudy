public class ThroughTheFog {
    public static void main(String[] args) {
        /*
         * 주어진 배열에 각 요소들을 끼리 빼고나서 남은 값을 절대값하여 다 더했을때, 가장 큰 값이 나오는 요소를 리턴하라.
         */
    }

    int absolutetValueSumMinimization(int[] a) {
        int compare = Integer.MAX_VALUE, test = 0, result = 0;

        for (int i = 0; i < a.length; i++) {
            test = 0;
            for (int j = 0; j < a.length; j++) {
                test += Math.abs(a[j] - a[i]);
            }
            if (test < compare) {
                result = a[i];
                compare = test;
            }
        }
        return result;
    }
}