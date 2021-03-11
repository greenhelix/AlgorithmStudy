import java.util.Arrays;

class LandOfLogic {
    public static void main(String[] args) {

    }

    // my
    String[] fileNaming(String[] names) {
        String[] check = Arrays.copyOf(names, names.length);
        int n = 1;
        for (int i = 1; i < names.length; i++) {
            for (int j = 0; j < i; j++) { // n요소가 0~(n-1)요소까지 같은 값인지를 확인.
                if (names[i].equals(names[j]) == true) { // 중복값이 있다..

                    if (names[i] != check[i]) { // 기존값과 change값이 다르다?
                        names[i] = check[i] + "(" + n + ")";
                        n++;
                        j = -1;
                        continue;
                    }
                    n = 1;
                    names[i] += "(" + n + ")";
                    j = -1;
                    n++;
                }
            }
        }
        return names;
    }

    // elite
    Object elitefileNaming(String[] names) {
        List<String> result = new ArrayList<>();
        for (String s : names) {
            if (result.contains(s)) {
                int i = 1;
                for (; result.contains(s + "(" + i + ")"); i++) {
                }
                s += "(" + i + ")";
            }
            result.add(s);
        }
        return result;
    }

}