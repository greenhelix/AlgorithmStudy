public class SmoothSailing {
    public static void main(String[] args){
    /*
    주어진 문자열에서 한글자의 위치를 지정햇을때, 두 문자열의 겹치는 문자가 있다면
    그것을 종합해주는데, 그 문자열의 겹치는 최소값을 출력합니다. 
    */
    }
    int commonCharacterCount(String s1, String s2){

        int [] a = new int [26];
        int [] b = new int [26]; 

        for(char c : s1.toCharArray()) a[c -'a']++;
        for(char c : s2.toCharArray()) b[c -'a']++;
        
        int total = 0; 
        for(int i=0;i<26; i++)
        total += Math.min(a[i], b[i]); 

        return total; 
    }
}