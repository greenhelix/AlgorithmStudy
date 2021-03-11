
public class TheJourneyBegins {
    public static void main(String[] args) {
        // 입력값이 몇 세기 인지 출력해주는 알고리즘
    }

    int centuryFromYear(int year) {
        int century = 0;

        if (year % 100 == 0) {
            century = year / 100;
        } else {
            century = year / 100 + 1;
        }
        return century;
    }

}
