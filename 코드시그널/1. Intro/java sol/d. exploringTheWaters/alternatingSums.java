public class ExploringTheWaters {
    public static void main(String[] args){
    /*
    사람이 한줄로 서있다. 두팀으로 교대로 나눈다. 
    그리고 각 팀의 합을 sum 배열에 넣는다. 
    */
    }

    int[] alternatingSums(int[] a) {
        int[] sum = new int [2]; 

        for(int i =0; i <a.length; i++){
            sum[i & 1] += a[i] ; 
        }
        return sum; 
    }
}
