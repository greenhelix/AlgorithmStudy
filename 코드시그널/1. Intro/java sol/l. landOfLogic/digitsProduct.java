class LandOfLogic {
    public static void main(String[] args) {

    }

    // my
    int digitsProduct(int product) {
        // 정수 곱이 주어지면 숫자가 곱과 같은 가장 작은 양의 정수를(0보다 큰 정수) 찾으십시오.
        // 그러한 정수가 없으면 대신 -1을 리턴하십시오.
        List<Integer> divisor1 = new ArrayList<Integer>();
        StringBuilder re = new StringBuilder();
        int show = product;
        if (product == 0) {
            System.out.println("0은 >> " + 10);
            return 10;
        } else if (product == 1) {
            System.out.println("1은 >> " + 1);
            return 1;
        } else if (product != 0 && product != 1) {

            for (int i = 9; i >= 1;) {
                if (product % i == 0) {
                    product = product / i;
                    divisor1.add(i);
                    System.out.print(divisor1 + "==> " + i);
                    i = 10;
                }
                i--;
                if (i == 1)
                    break;
            }
            int mul = 1;
            for (int a : divisor1) {
                mul *= a;
            }
            if (mul != show) {
                return -1;
            }
            System.out.print(divisor1);
        } else {
            return 10;
        }

        for (int i = divisor1.size() - 1; i >= 0; i--) {
            re.append(divisor1.get(i));
        }

        return Integer.parseInt(re.toString());
    }

    // elite
    int elitedigitsProduct(int product) {
        if (product == 0)
            return 10;
        if (product < 10)
            return product;

        String r = "";
        for (int d = 9; d > 1; d--)
            for (; product % d == 0; product /= d)
                r = d + r;
        return product == 1 ? new Integer(r) : -1;
    }

}