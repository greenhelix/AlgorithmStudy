public class eruptionOfLight {
    public static void main(String[] args) {
        // 주어진 문자열을 검사하여 회문이 되는 조건으로 만들어준다.
        // 회문은 최소문자를 추가하여 완성시킨다.
    }

    // my
    String buildPalindrome(String st) {
        StringBuilder stst = new StringBuilder(st).reverse();
        StringBuilder newSt = new StringBuilder(st);

        if (st.equals(stst.toString())) {
            return st;
        } else if (st.equals(stst) == false) {
            StringBuilder bucket = new StringBuilder();
            while (true) {
                stst = stst.reverse();
                bucket.append(stst.charAt(0));
                stst = stst.deleteCharAt(0);
                if (stst.toString().equals(stst.reverse().toString()) == true) {
                    bucket.reverse();
                    newSt = newSt.append(bucket);
                    break;
                }
            }
            return newSt.toString();
        }
        return "something wrong!";
    }
}