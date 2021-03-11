class LandOfLogic {
    public static void main(String[] args) {

    }

    // my
    String messageFromBinaryCode(String code) {
        StringBuilder sb = new StringBuilder();
        Arrays.stream(code.split("(?<=\\G.{8})")).forEach(s -> sb.append((char) Integer.parseInt(s, 2)));
        String out = sb.toString();
        return out;
    }

    // elite
    String elitemessageFromBinaryCode(String code) {
        return new String(new BigInteger(code, 2).toByteArray());
    }

}