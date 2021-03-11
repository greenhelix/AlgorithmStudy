import java.util.ArrayList;

public class DivingDeeper {
    public static void main(String[] args) {
        /**
         * 주어진 숫자 배열을 kㅓ배수 -1 자리의 요소를 제거하라.
         */
    }

    int[] extractEachKth(int[] input, int k) {
        int j = k - 1, x = 1, y = 0;
        ArrayList<Integer> hey = new ArrayList<>();

        for (int a : input) {
            hey.add(a);
        }
        for (int i = 0; i < hey.size(); i++) {
            if (i == j && i > 0) {
                hey.remove(i);
                x++;
                j = (k - 1) * x;
            } else if (j == 0) {
                hey.clear();
            }
        }
        int[] out = new int[hey.size()];

        for (int last : hey) {
            out[y++] = last;
        }
        return out;
    }
}