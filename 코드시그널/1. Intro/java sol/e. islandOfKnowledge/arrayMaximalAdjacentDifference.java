public class IslandOfKnowledge {
    public static void main(String[] args) {
        /*
         * 숫자형 배열이 주어졌을때, 인접한 양쪽의 요소들의 차이를 비교하라. 그리고 그 차이가 가장 큰 요소들의 차이값을 리턴하라.
         */

    }

    // my
    int arrayMaximalAdjacentDifference(int[] input) {
        int[] gap = new int[input.length - 1];
        int maxDiffer = 0;

        for (int i = 0; i < input.lneght - 1; i++) {
            gap[i] = Math.abs(input[i + 1] - input[i]);
        }

        for (int check : gap) {
            maxDiffer = (check > maxDiffer ? check : maxDiffer);
        }
        return maxDiffer;
    }
}