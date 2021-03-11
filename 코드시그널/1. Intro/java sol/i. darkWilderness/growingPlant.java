public class DarkWilderness {
    public static void main(String[] args) {
        // 그냥 식물이 자라는데, 낮에는 크고 저녁에는 줄어듬 ㅋ
        // 그리고 DesiredHeigth가 되면, 리턴하라는 건데, 몇일이 걸렸는지.

    }
    int growingPlant(int upSpeed, int downSpeed, int desiredHeight) {
        int growth = upSpeed;
        int not = upSpeed - downSpeed;
        int i = 1, count = 1;
        if (growth > desiredHeight) {
            return count;
        }
        for (;; i++) {
            growth = i * not + upSpeed;
            if (desiredHeight <= growth) {
                count = i + 1;
                break;
            }
        }
        return count;
    }
}
