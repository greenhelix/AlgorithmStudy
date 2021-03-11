import java.util.Arrays;

public class eruptionOfLight {
    public static void main(String[] args) {
        // 문자열에서 알파벳 시퀀스가 유지되는지 확인.
        // 문자열에서 해당 알파벳 갯수가 이전 알파벳 갯수보다 많으면 안됨.
        // 1. A B C D.. 이런식으로 시퀀스가 있어야함. (순서는 상관없음)
        // 2. AAABBC... 와 같이, A가 3개 일때, B는 3개이하여야함. C는 B기준으로 B의 갯수이하여야함.
        // 3. BBBCCD ... A 가 빠져 있으므로 시퀀스가 유지안됨..

    }

    // my
    boolean isBeatifulString(String input) {
        int[] line = new int[26];
        for (int i = 0; i < input.length(); i++) {
            line[input.charAt(i) - 'a']++;
        }
        System.out.println(Arrays.toString(line));

        for (int a = 1; a < line.length; a++) {
            if (line[a - 1] < line[a]) {
                System.out.println("more than");
                return false;
            } else if (line[a] == 0) {
                System.out.println("zero find");
                int zeroSum = 0;
                for (int z = a; z < line.length; z++) {
                    zeroSum += line[z];
                }
                if (zeroSum == 0) {
                    System.out.println("after zero all");
                    return true;
                }
            }
            System.out.println("nothing problem");
            return true;
        }
    }
}