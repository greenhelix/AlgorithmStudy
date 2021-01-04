import java.util.Arrays
import java.util.Stack
class MySolution {
    fun solution(board: Array<IntArray>, moves: IntArray): Int {
        var answer = 0
        var s = Stack<Int>()
        for(i in moves){
            println("$i 칸꺼내기")
            println(Arrays.toString(board[i-1]))
            for( j in board[i-1].reversed()){
                println(j)
                s.push(j)
                // board[i-1].remove(board[i-1].size()-1)
                print(Arrays.toString(board[i-1]))
                
                break
            }
            println()
        }
        print("$s 는 이거다.")
        return answer
    }
}
//반드시 비교해본다. 답안이랑.