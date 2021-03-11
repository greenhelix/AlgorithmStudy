
public class matrixElementsSum {
    public static void main(String[] args) {
    //바둑판같은데에 숫자들이 들어있다고 생각한다. 
    //각 행에서 0이 발견되면, 그 아래의 열의 값들은 다 무시된다. 
    //만약 행의 요소들에 0이 아니라면 계속 더해간다. 
    //즉 계산을 세로방향으로 진행하게 한다. 
    }

    int matrixElementsSum(int [][] matrix){
        int total = 0; 
        for(int i =0; i<matrix[0].length; i++){
            for(int j =0; j<matrix.length; j++){
                if(matrix[i][j] == 0){
                    System.out.println(i+1+"행"+(j+1)+"번째에 유령이 나타남. 밑에는 버릴것."); 
                    break; 
                }else total += matrix[i][j]; 
            }
        }
        return total;
    }
   
}