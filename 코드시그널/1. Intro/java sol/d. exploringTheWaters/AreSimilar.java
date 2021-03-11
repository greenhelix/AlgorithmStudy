public class ExploringTheWaters {
    public static void main(String[] args){
       /*
        두개의 배열에서 한쌍이 다르다면 그것을 다시 넣어주어 비슷하게 배열을 만들어주는 것이다. 
       */
}
    boolean areSimilar(int[] a, int[] b){
        int differ = 0; 
        Set s1 = new HashSet(); 
        Set s2 = new HashSet(); 

        for(int i =0; i< a.length; i++){
            if(a[i] != b[i]){
                differ++; 
                s1.add(a[i]);
                s2.add(b[i]);
            }
        }
        if(differ == 0) return true; 
        else if(differ == 2 && s1.equals(s2)) return true;
        else return false; 
    }

}