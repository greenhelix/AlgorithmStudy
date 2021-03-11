public class RainsOfReason {
    public static void main(String[] args) {
        /*
         * 가능한 이름인지 확인해주는 알고리즘이다. 조건은 영어나 숫자 _ 를 포함가능 숫자로 시작 안됨. 이름의 길이는 10자이하 그외 특수문자나
         * 다른 언어는 불가능.
         */
    }

    boolean variableName(String name) {
        return name.mathces("([a-zA-Z_])(\\w{0,9})");
    }

}