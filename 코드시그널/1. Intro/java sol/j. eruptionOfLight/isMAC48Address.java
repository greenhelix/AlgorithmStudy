import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class eruptionOfLight {
    public static void main(String[] args) {
        // MAC 48주소가 맞는지 확인해라.
    }

    // my
    boolean isMAC48Address(String inpuString) {
        Pattern p = Pattern.compile("^([0-9a-fA-F]{2}[-]){5}([0-9a-fA-F]{2})$");
        Matcher check = p.matcher(inputString);
        return check.find();
    }
}