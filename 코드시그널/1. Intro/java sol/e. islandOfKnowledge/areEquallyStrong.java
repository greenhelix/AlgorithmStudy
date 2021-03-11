public class IslandOfKnowledge {
    public static void main(String[] args) {
        /*
         * 나와 친구의 양팔의 힘을 수치로 측정했을때, 각자의 양팔의 힘을 합쳤을 때 같아야하는데, 같으면 true 다르면 false 를 반환한다.
         */

    }

    // my
    boolean areEquallyStrong(int yourLeft, int yourRight, int friendsLeft, int friendsRight) {

        boolean equality = true;
        int yourPower = 0;
        int friendPower = 0;

        yourPower = yourLeft + yourRight;
        friendPower = friendsLeft + friendsRight;

        if (yourPower == friendPower) {
            int yourMax = 0;
            int friendMax = 0;

            yourMax = Math.max(yourRight, yourLeft);
            friendMax = Math.max(friendsRight, friendsLeft);

            if (yourMax == friendMax) {
                return equality = true;
            } else if (yourMax != friendMax) {
                return equality = false;
            }
        } else {
            return equality = false;
        }
        return equality;
    }
}