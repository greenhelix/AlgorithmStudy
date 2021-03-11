public class RainsOfReason {
    public static void main(String[] args) {
        /*
         * 입력값으로 바꿀 번호와 무엇이 바꿀지 설정한다. 그리고 입력값에 바꿀 번호와 같은 숫자가 있다면, 그것들을 다 바꿀 숫자로 바꿔주는
         * 알고리즘이다.
         */

    }

    int[] arrayReplace(int[] input, int changeNum, int whatChange) {
        for (int i = 0; i < input.length; i++) {
            input[i] = input[i] == changeNum ? whatChange : input[i];
        }
        return input;
    }
}