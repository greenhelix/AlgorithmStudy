public class ThroughTheFog {
    public static void main(String[] args) {
        /*
         * 주어진 수를 -1 해서 원으로 둘러 쌌을때, 픽된 수의 맞은편 수는 무엇인지 리턴하라는 알고리즘이다.
         */
    }

    int circleOfNumbers(int n, int pick) {
        int result = 0;
        if (pick < n / 2) {
            result = n / 2 + pick;
        } else {
            result = n / 2 + pick - n;
        }
        return result;
    }
}