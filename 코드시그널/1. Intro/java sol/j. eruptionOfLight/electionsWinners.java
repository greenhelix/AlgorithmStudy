public class eruptionOfLight {
    public static void main(String[] args) {
        // 후보자들이 존재하고, 그들의 표현황이 주어진다.
        // 여기서 k는 남은 표의 수이다. 이것을 통해서 승리자가 될 수 있는
        // 후보자수를 선별해라.
    }

    // my
    int electionsWinners(int[] votes, int k) {
        int result = votes.length;
        int[] elect = new int[votes.length];
        if (k == 0) {
            System.out.println("no more votes...");
            Arrays.sort(votes);
            if (votes[votes.length - 1] == votes[votes.length - 2]) {
                return 0;
            } else {
                return 1;
            }
        } else if (k != 0) {
            for (int i = 0; i < votes.length; i++) {
                elect[i] = votes[i] + k;
            }
            for (int i = 0; i < votes.length; i++) {
                for (int j = 0; j < votes.length; j++) {
                    if (elect[i] <= votes[j]) {
                        result--;
                        break;
                    }
                }
            }
        }
        System.out.println("final result is .." + result + "people can be a Winner!!");
        return result;
    }

    // elite
    int elite_electionsWinners(int[] votes, int k) {
        int max = Arrays.stream(votes).max().getAsInt();
        System.out.println(max);
        return k == 0 ? Arrays.stream(votes).filter(x -> x == max).count() == 1 ? 1 : 0
                : (int) Arrays.stream(votes).filter(x -> x + k > max).count();
    }
}