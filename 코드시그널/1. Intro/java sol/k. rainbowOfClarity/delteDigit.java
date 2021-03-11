import java.util.ArrayList;
import java.util.List;

class RainbowOfClarity {
    public static void main(String[] args) {
        // 주어진 숫자에서 어느 자릿수 한자리를 빼냈을때,
        // 값이 가장 큰 경우는 어떤 수인가.

        // 모든 수를 배열이나 리스트로 만들고
        // 각 자리이 한자리씩 다 빼보고 그서을 배열에 넣어준다.
        // 그리고 나서 stream max()를 통해 최대 값이 무엇인지
        // 확인하고 형변환을 하여 리턴해준다.
    }

    // my
    int deleteDigit(int n) {
        String sample = Integer.toString(n);
        int size = sample.length();
        char temp[] = new char[size];
        List<Character> check1 = new ArrayList<Character>();

        for (int i = 0; i < size; i++) {
            temp[i] = sample.charAt(i);
        }
        for (char a : temp) {
            check1.add(a);
        }
        List<Character> check2 = new ArrayList<Character>();
        List<Integer> results = new ArrayList<Integer>();
        StringBuilder let = new StringBuilder();
        char temp2[] = new char[size - 1];

        check2.addAll(check1);
        int scale = 0;
        int comb = 0;

        for (int i = 0; i < check1.size(); i++) {
            check1.remove(i);
            for (char b : check1) {
                temp2[scale++] = b;
            }
            scale = 0; // scale 초기화
            comb = Integer.parseInt(let.append(temp2).toString());
            results.add(comb);
            let.setLength(0); // stringbuilder초기화
            check1.clear(); // check1초기화
            check1.addAll(check2); // check1을 원래 상태로 돌려줌.
        }
        return results.stream().max(Integer::compare).orElse(-1);
    }

    // elite
    int eliteDeleteDigit(int n) {
        int max = 0;
        for (int i = 0; i < n; i *= 10)
            max = Math.max(n / 10 / i * i + n % i, max);
        return max;
    }
}