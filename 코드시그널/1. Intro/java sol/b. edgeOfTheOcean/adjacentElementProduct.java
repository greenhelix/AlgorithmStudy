
public class adjacentElementProduct {
    public static void main(String[] args) {
        // 바로 옆 요소들끼리 서로 곱하여서 가장 큰 값을 리턴하는 알고리즘.
    }

    int adjacentElementsProduct(int[] i) {
        int max = i[0] * i[1];

        for (int x = 2; x < i.length; x++)
            if (max < i[x = 1] * i[x])
                max = i[x - 1] * i[x];

        return max;
    }
}