public class IslandOfKnowledge {
    public static void main(String[] args) {
        /*
         * 주어진 숫자형 배열에서 숫자들의 좌표는 장애물이 된다. 이동은 양수 방향으로 진행되며, 해당 장애물들의 사이로만 점프가 가능하다. 그
         * 점프거리의 최소값을 반환하라는 알고리즘이다.
         */
    }

    // my
    int avoidObstacles(int[] put) {
        for (int i = 2;; i++) {
            boolean t = true;
            for (int n : put)
                t = t && n % i != 0;
            if (t)
                return i;
        }
    }
}