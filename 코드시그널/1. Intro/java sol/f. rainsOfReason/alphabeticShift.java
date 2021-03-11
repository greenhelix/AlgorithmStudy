public class RainsOfReason {
    public static void main(String[] args) {
        /*
         * 입력값이 알파벳인데, 그 입력문자열들의 알파벳을 다음 문자로 바꿔주는 것이다. abcd라면, bcde로 바꿔주는 것이다. z 라면 다시 a
         * 로 바꿔준다. 한 칸씩 밀어준다고 생각하면됨.
         */
    }

    String alphabeticShift(String input) {
        char[] seperate = input.toCharArray();
        String result = "";

        for (int i = 0; i < seperate.length; i++) {
            if (seperate[i] == 'z') {
                seperate[i] = 'a';
            } else {
                seperate[i] += 1;
            }
        }
        for (int j = 0; j < seperate.length; j++) {
            result += Character.toString(seperate[j]);
        }
        return result;
    }
}