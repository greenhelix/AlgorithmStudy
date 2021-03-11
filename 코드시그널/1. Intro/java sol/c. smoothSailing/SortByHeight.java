public class SmoothSailing{
    public static void main(String[] args){
        /*
        -1을 제외하고 다른 나머지 수들을 순서대로 오름차순으로 나열해주는 것이다. 
        */
    }
   int[] sortByHeight(int[] a){
       List b = new Vector(); 
       
       for(int i : a) if(i > -1) b.add(i);

       Collections.sort(b);
       Iterator it = b.iterator(); 

       for(int i =0; i<a.length; i++){
           if(a[i] > -1) a[i] = (Integer)it.next();}
       return a; 
   }
}