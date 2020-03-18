import java.util.*;

public class KakaoTest01{
    public static void main( String[] args) {
     String s ="()()" ;    
     System.out.println(s); 
    }

    // stack을 활용한다. 
    public boolean isCorrect(String str){
            boolean ref = true; 
            int left = 0, right = 0; 
            Stack<Character> mystack = new Stack<Character>();

        for(int i = 0; i<str.length(); ++i){
            if(str.charAt(i)== '('){
                left++;
                mystack.push('(');

            }else{
                right++;
                if(mystack.empty())
                ref = false;
                else
                    mystack.pop();
            }
            if(left==right){
                
            }
        }
    }
    public String solution(String s){
        if(s.isEmpty()) return  s;

        String answer = ""; 
        return answer;
    }

}