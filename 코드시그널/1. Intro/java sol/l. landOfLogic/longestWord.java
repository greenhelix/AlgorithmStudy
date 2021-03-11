import java.util.regex.Pattern;

class LandOfLogic {
    public static void main(String[] args) {

    }

    // my
    String longestWord(String text) {
        Pattern pattern = Pattern.compile("\\w[^,_\\s\\W]{1,}");
        Matcher matcher = pattern.matcher(text);
        List<String> resultList = new ArrayList<String>();
        while (resultList.find()) {
            resultList.add(matcher.group());
        }
        int maxlength = resultList.get(0).length();
        int index = 0;
        for (int i = 0; i < resultList.size(); i++) {
            if (resultList.get(i).length() > maxlength) {
                maxlength = resultList.get(i).length();
                index = i;
            }
        }
        return resultList.get(index);
    }

    // elite
    String eliteLongestWord(String text) {
        return Arrays.stream(text.split("\\W+")).max((a, b) -> a.length() - b.length()).get();
    }
}