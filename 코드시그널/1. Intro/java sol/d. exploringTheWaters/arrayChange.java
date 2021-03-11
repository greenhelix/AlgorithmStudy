public class ExploringTheWaters {
    public static void main(String[] args) {
        /*
         * 입력된 배열의 값들에서 앞수가 뒷수보다 크거나 같을 경우 뒷수에 변화를 주어 증가하는 시퀀스를 형성시키라는 문제. 배열에 변화를 주어
         * 시퀀스를 유지시켜라. 증가하는 시퀀스로.
         */
    }

    int arrayChange(int[] input) {
        int change = 0;
        for (int i = 0; i < input.length - 1; i++) {

            if (input[i] >= input[i + 1]) {
                change += input[i] + 1 - input[i + 1];
                input[i + 1] = input[i] + 1;
            }
        }
        return change;
    }
}