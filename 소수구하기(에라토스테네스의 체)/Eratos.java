import java.util.List;
import java.util.ArrayList;

class Cls_Eratos {
    public static void main(String[] args) {
        // 에라토스테네스이 체
        // 주어진 수의 범위내에 소수들을 찾아내는 알고리즘이다.
        // 2는 소수이므로 오른쪽에 2를 쓴다. (빨간색)
        // 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다.
        // 자기 자신을 제외한 2의 배수를 모두 지운다.
        // 남아있는 수 가운데 3은 소수이므로 오른쪽에 3을 쓴다. (초록색)
        // 자기 자신을 제외한 3의 배수를 모두 지운다.
        // 남아있는 수 가운데 5는 소수이므로 오른쪽에 5를 쓴다. (파란색)
        // 자기 자신을 제외한 5의 배수를 모두 지운다.
        // 남아있는 수 가운데 7은 소수이므로 오른쪽에 7을 쓴다. (노란색)
        // 자기 자신을 제외한 7의 배수를 모두 지운다.

        // 위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다.
        int answer = Eratos(345);
        System.out.println(answer);

    }

    public static int Eratos(int input) {

        List<String> show = new ArrayList<String>();

        for (int i = 2; i <= input; i++) {
            show.add(Integer.toString(i));
        }
        int[] prime = { 2, 3, 5, 7 };

        int start = 0;
        for (int j = start; j < 4; j++) {
            for (int i = j + 1; i < show.size(); i++) {
                String check = show.get(i);
                if (Integer.parseInt(check) % prime[j] == 0) {
                    show.remove(check);
                }
            }
        }
        System.out.println(
                "===============================================================================================");
        System.out.println(show);

        return show.size();
    }

}
