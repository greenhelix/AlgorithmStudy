public class SmoothSailing{
    public static void main(String[] args){
        /*
        ()안에 있는 문자를 거꾸로 해주면서 ()는 빼준다. 
        문자열 안에 이 문자열을 거꾸로하면서 괄호를 제거해주면 된다. 
        */

    }
   String reverseInParentheses(String a){
       int rStart = 0; 
       int rEnd = a.length() -1; 
       
       for(int i=0; i < a.length(); i++){
           if(a.charAt(i) == '('){ rStart = i; }
           if(a.charAt(i) == ')'){ 
                rEnd = i; 
                String temp = a.substring(rStart +1, rEnd); 
            return reverseInParentheses(a.substring(0, rStart)+ reverseString(temp)
            + a.substring(rEnd +1)); } 
        }
       return a; 
   }
   String reverseString(String b){
       char [] test = b.toCharArray(); 
       String show = ""; 
       for(int i = test.length-1; i>=0; i--){
           show += Character.toString(test[i]);}
       return show; 
   }
}