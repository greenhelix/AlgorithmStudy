
public class shpaeArea {
    public static void main(String[] args) {
        // 도형의 갯수가 점점 늘어나는 알고리즘..
        // // n = 1 >>> 1
        // n = 2 >>> 1+4= 5
        // n = 3 >>> 1+4+8=13
        // n = 4 >>> 1+4+8+12=25
        // 1 이후로 4의 배수가 더해지므로 그것을 고려해서 규칙을 만든다.
    }

    int shapeArea(int n) {
        int sum = 1;

        for (int i = 1; i < n; i++)
            sum += 4 * i;
        return sum;
    }
}