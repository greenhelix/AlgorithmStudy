public class newRoadSystem {
    public static void main(String[] args) {
        
    }
    boolean newRoadSystem(boolean[][] roadRegister) {
        int [] column = new int[roadRegister[0].length]; // 가로
        int [] row = new int[roadRegister.length]; //세로
        for(int i = 0; i< roadRegister.length; i++){
            for(int j = 0; j< roadRegister[0].length; j++){
            if(roadRegister[i][j] == true){
                row[i] += 1;
                column[j] +=1;}}}
        return Arrays.equals(row,column);
    }
}