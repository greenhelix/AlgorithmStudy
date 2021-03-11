public class darkWilderness {
    public static void main(String[] args) {

    }

    // my
    int digitDegree(int n) {
        int result = 1;
        int test = sum(integerToInt(n));
        if (n / 10 == 0) {
            return 0;
        }
        while (true) {
            if (Integer.toString(test).matches("[0-9]")) {
                return result;
            } else {
                test = sum(integerToInt(test));
                result++;
            }
        }
    }

    static int sum(Integer[] x) {
        int z = Stream.of(x).reduce(0, (a, b) -> {
            return a + b;
        });
        return z;
    }

    static Integer[] integerToInt(int x) {
        int[] num = Stream.of(String.valueOf(x).split("")).mapToInt(Integer::valueOf).toArray();
        Integer[] digits = Arrays.stream(num).boxed().toArray(Integer[]::new);
        return digits;
    }

    // elliete
    int digitDegree2(int n) {
        if (n / 10 == 0)
            return 0;
        int num = 0;
        while (n != 0) {
            num += n % 10;
            n /= 10;
        }
        int result = 1 + digitDegree2(num);
        return result;
    }
}