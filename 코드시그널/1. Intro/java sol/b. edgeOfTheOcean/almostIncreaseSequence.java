public class almostIncreaseSequence {
    public static void main(String[] args) {
        // 증가하는 수의 나열을 나타내보라는 것이다.
        // 단 조건이 있는데, 만약 한 개의 수가 그 시퀀스를 막는다면
        // 그 한개의 수를 제거하는 조건으로 시퀀스가 유지되는지 확인하라는 알고리즘.

    }

    boolean almostIncreasingSequence(int[] sequence) {
        int length = sequence.length;
        int a = -1, b = 0;

        for (int i = 1; i < length; i++) {

            if (sequence[i - 1] >= sequence[i]) {
                a = i;
                b++;
            }
            if (b > 1) {
                System.out.println("one 앞에수가 큰 경우나 같은 경우 2번이상 나옴");
                return false;
            }
            if (b == 0) {
                System.out.println("two 안건드령도 시퀀스 유지 잘됨."); 
                return true; 
            }
            if (a == length-1 || a== 1){
                System.out.println("a = "+a); 
                System.out.println("three 한개의 수를 빼면 성립됨."); 
                return true; 
            }
            if (sequence[a-1] < sequence[a+1]){
                System.out.println("a= "+a); 
                System.out.println("four 양쪽 중 하나를 잘라내면 시퀀스 성립."); 
                return true; 
            }
            if (sequence[a-2] <sequence[a]){
                System.out.println("a = "+a); 
                System.out.println("five 공갈빵 하나 빼면 시퀀스 성립"); 
                return true; 
            }
            System.out.println("a = "+a +" 이상한 경우"); 
            return false; 
        }
        return false;
    }
}