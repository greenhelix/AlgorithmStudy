import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class darkWilderness {
    public static void main(String[] args) {
        // 주어진 문자열에서, 숫자접미사만 뽑아내라 
    }
    // my
    String longestDigitsPrefix(String input) {
        String result = "";
        Pattern pattern = Pattern.compile("^[0-9]+");
        Matcher xray = pattern.matcher(input);
        if (xray.find()) {
            result = input.substring(xray.start(), xray.end());
        }
        return result;
    }
    // elliete
    String longestDigitsPrefix2(String input) {
        return input.replaceAll("^(\\d*).*", "$1");
    }
}
