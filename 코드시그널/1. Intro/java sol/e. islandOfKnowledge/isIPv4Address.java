import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;

public class IslandOfKnowledge {
    public static void main(String[] args) {
        /*
         * ip 주소의 정확성을 판단해주라는 알고리즘이다. 정규식을 활용해서 간단하게 아이피 주소의 유무를 확인해줄 수 있다.
         */

    }

    // my
    boolean isIPv4address(String input) {
        if (input == null || input.isEmpty()) {
            return false;
        }
        input = input.trim();

        if ((input.length() < 6) || (input.length() > 15)) {
            return false;
        }
        try {
            Pattern pattern = Pattern.compile("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.)" + "{3}"
                    + "(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$");
            Matcher matching = pattern.matcher(input);

            if (matching.matches() == true) {
                System.out.println("perfect");
            } else {
                System.out.println("nope");
            }
            return matching.matches();
        } catch (PatternSyntaxException ex) {
            System.out.println("sync error");
            return false;
        }
    }
}