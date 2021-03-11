
public class TheJourneyBegins {
    public static void main(String[] args) {
        // 회문 확인 알고리즘 단순 확인만.
    }

    boolean checkPalindrome(String a) {
        String string2 = new StringBuilder(a).reverse().toString();

        if (a.equals(string2)) {
            return true;
        } else {
            return false;
        }
    }
}