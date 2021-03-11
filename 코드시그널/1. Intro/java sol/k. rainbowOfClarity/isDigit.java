import java.util.regex.Pattern;

class RainbowOfClarity {
    public static void main(String[] args) {

    }

    // my
    boolean isDigit(char symbol) {
        return Pattern.compile("^([0-9]$)").matcher(String.valueOf(symbol)).matches();
    }
    // elite

}