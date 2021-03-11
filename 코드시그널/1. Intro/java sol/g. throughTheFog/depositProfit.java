public class ThroughTheFog {
    public static void main(String[] args) {
        /*
         * 예금의 타겟금액까지 가려면, 이자율을 고려했을때, 얼마나 걸리나 리턴해주는 알고리즘이다.
         */
    }

    int depositProfit(int deposit, int rate, int target) {
        double realRate = (double) reate / 100 + 1;
        double howMuch = (double) target / deposit;
        double yearDetail = houMany(howMuch, realRate);
        int resultYear = (int) Math.ceil(yearDetail);

        return resultYear;
    }

    static double howMany(double x, double base) {
        return Math.log10(x) / Math.log10(base);
    }
}