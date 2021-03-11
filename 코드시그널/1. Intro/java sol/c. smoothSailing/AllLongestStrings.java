public class SmoothSailing {
    public static void main(String[] args){
        //주어진 문자열 배열에서 가장 문자열이 긴 요소를 찾아서 배열에 넣고 그것을 반환
        //하라는 문제이다. 
}

    String[] allLongestStrings(String[] inputArray) {
    
    //  max lenght 을 나타내는 숫자형 객체 생성 
    int mL = 0 ; 
    
    // 배열 각 요소를 돌면서 가장 긴 요소가 무엇이고 그것의 길이가 몇인지 알아내는 반복문
    for(int i =0; i < inputArray.length; i++){
        
        if(mL<inputArray[i].length())
            mL = inputArray[i].length();
    }
    
    //최종적으로 제일 긴 글자를 찾아내면 그 길이를 longest에 고정으로 박는다.
    final int longest = mL;
    
    System.out.println("mL ="+longest);
    
    // 그리고, 기존 배열에서 가장 긴 아까 longest의 수에 해당하는 길이를 가진 
    // 요소를 찾아내서 그것들만 따로 다시 새로운! 
    // 배열로 생성해서 리턴한다. 
    return Stream.of(inputArray)
        .filter(s -> s.length()==longest)
        .toArray(String[]:: new); 
    
    }

}
