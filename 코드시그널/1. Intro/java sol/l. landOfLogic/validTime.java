class LandOfLogic {
    public static void main(String[] args) {
        // 24시간 체제안의 합리적인 시간인지 확인해줘라.
    }

    // my
    boolean validTime(String time) {
        return time.matches("^([01][0-9]|[2][0-3]):([0-5][0-9])$");
    }
}