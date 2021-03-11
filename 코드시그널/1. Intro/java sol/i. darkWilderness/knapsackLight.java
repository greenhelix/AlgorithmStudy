public class darkWilderness {
    public static void main(String[] args) {
        // 두가지 답안이있음.
        // 하나느 내가 하나느 앨리트가.
        // 조건이 최대 무게가 있고, 각 물품의 가치와 무게가 있음
        // 물품은 총 2개이고, 각 가치값이 있는데,
        // 최대 무게 조건과 물품의 무게 조건이 각 경우마다
        // 물품을 가져갈 값이 달라짐. 상황마다 다른데, 그
        // 경우를 분간해주라는 알고리즘.
    }

    // my solution
    int knapsackLight1(int v1, int w1, int v2, int w2, int max) {

        int result = 0;
        if (max == w1 && max == w2) {
            result = max;
        } else if (max == w1) {
            if (max < w2) {
                result = v1;
            } else if (max > w2) {
                result = v2;
            }
        } else if (max == w2) {
            if (max < w1) {
                result = v2;
            } else if (max > w1) {
                result = v1;
            }
        } else if (max < w1 && max < w2) {
            result = 0;
        } else {
            result = w1 + w2 <= max ? v1 + v2 : Math.max(v1, v2);
        }
        return result;
    }

    // elliete solution
    int knapsackLigh2t(int v1, int w1, int v2, int w2, int max) {
        if (w1 > max && w2 > max) {
            return 0;
        }
        if (w1 + w2 <= max) {
            return v1 + v2;
        }
        if (w1 > max) {
            return v2;
        }
        if (w2 > max) {
            return v1;
        }
        return Math.max(v1, v2);
    }
}