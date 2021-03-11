class LandOfLogic {
    public static void main(String[] args) {

    }

    // my
    int sumUpNumbers(String inputString) {
        Matcher check = Pattern.compile("\\d{1,}").matcher(inputString);
        List<String> result = new ArrayList<String>();
        int sum = 0;
        while (check.find()) {
            result.add(check.group());
        }
        for (int i = 0; i < result.size(); i++) {
            sum += Integer.parseInt(result.get(i));
        }
        return sum;
    }

    // elite
    int elitesumUpNumbers(String inputString) {
        Matcher m = Pattern.compile("\\d+").matcher(inputString);
        int sum = 0;
        while (m.find()) {
            sum += Integer.parseInt(m.group(0));
        }
        return sum;
    }

}