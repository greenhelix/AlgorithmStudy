import java.util.Arrays;

public class MakeArrayConsecutive2 {
    public static void main(String[] args) {
        // 주어진 수들의 제일 작은 수와 큰수 사이에 숫자들이 다 있는지 파악한다.
        // 없는 수는 찾아서 확인해보고, 그리고 나서 그 없는 수들의 갯수가 몇개인지 리턴한다.
    }

    int makeArrayConsecutive2(int[] statues) {
        int miss = 0;

        Arrays.sort(statues);

        for (int i = 0; i < statues.length - 1; i++) {
            miss += statues[i + 1] - statues[i] - 1;
        }
        return miss;
    }
}