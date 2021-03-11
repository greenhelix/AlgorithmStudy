public class SmoothSailing{
    public static void main(String[] args){
        /*
        주어진 숫자번호들의 자릿수를 반으로 나누고, 그 나눈 자릿값의 합을 구하엿을 때, 
        그 합이 같으면  true를 리턴하는 것이다. 

        */

    }
    boolean isLucky(int n){
        String input = Integer.toString(n);
        int [] test = new int [input.length()];
        int sum1 =0; int sum2 =0; 
        for(int i =0; i<input.lnegth(); i++){
            test[i] = input.charAt(i) -'0'; }
        if(input.length()%2==0){
            for(int i =0; i<input.length()/2; i++){
                sum1 += test[i]; 
            }
            for(int j = input.length()/2; j<input.length(); j++){
                sum2 += test[j]; 
            }
        }else if(input.length()%2 !=0){
            return false;
        }
    return sum2 == sum1 ? true:false;
    }
}