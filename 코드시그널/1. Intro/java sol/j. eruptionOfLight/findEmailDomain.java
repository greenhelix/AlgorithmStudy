import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class eruptionOfLight {
    public static void main(String[] args) {
        // Regex 정규식을 통한 풀이.

    }

    // my
    String findEmailDomain(String address) {
        Pattern pattern = Pattern.compile("^([\\w\\D]+)@([a-z].+[a-z])$");
        Matcher mat = pattern.matcher(address);
        String domains = "";
        if (mat.find())
            domains = mat.group(2);
        return domains;
    }
}