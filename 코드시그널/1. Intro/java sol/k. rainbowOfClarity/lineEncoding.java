class RainbowOfClarity {
    public static void main(String[] args) {

    }

    // my
    String lineEncoding(String s) {
        s += "#";
        System.out.println(s);
        int cnt = 1;
        StringBuilder result = new StringBuilder();

        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                cnt++;
            } else {
                if (cnt > 1) {
                    result.append(cnt);
                    System.out.println(result);
                }
                result.append(s.charAt(i - 1));
                System.out.println(result);
                cnt = 1;
            }
        }
        return result.toString();
    }
    // elite

}