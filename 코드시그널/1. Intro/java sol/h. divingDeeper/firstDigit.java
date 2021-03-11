public class DivingDeeper {
    public static void main(String[] args) {
        /**
         * 입력된 문자열에서 문자를 제외한 숫자만 출력하는 정규식 알고리즘
         */
    }

    char firstDigit(String input) {
        return input.replaceAll("[^0-9]", "").charAt(0);
    }
}