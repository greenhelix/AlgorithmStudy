import java.util.* //java 유틸을 다 포함시켜준다.
// 문제 파악을 잘못했다. 결국 00000 00103 02501 42442 35131 이 따로가 아니라 한 폭으로 봤어야했다.
// 즉 아래와 같이 문제를 봐야한다. 
// 00000
// 00103
// 02501
// 42442
// 35131  이렇게 봐야한다. 여기서 1번 위치에서 나올 값이 4 임을 알 수 있다!!!
class StackSolution{
    // 다차원 배열로 board가 들어오고, 숫자 배열로 moves가 입력된다. 리턴값은 int여야 한다.
    fun stacksolution(board: Array<IntArray>, moves: IntArray): Int{
        var answer = 0 

        // 여기서 부터 풀이
        val stack = Stack<Int>() // 스택을 불러서 선언해준다. <>안에다 원하는 형을 입력

        // moves에 있는 값들인 주소록같은 것을 forEach로 각 값을 it에 담아서 반복한다. 따로 선언안하면 it으로 사용한다.
        moves.forEach {  
            for(i in board.indices) //for 문으로 board에 있는 것을 indices즉 인덱스형태로 i에 넣어서 뿌려준다.
            { // i 는 0,1,2,3,4 가 될것이다.
                if(board[i][it-1] != 0 ){ //  forEach에서 나온 it이 여기서 부터 사용된다. 즉, 해당 주소를 찾기위해 이중배열의 두번째 인자로 들어간다.
                    print("now: ")
                    println(board[i][it-1])
                    if(stack.isNotEmpty() && stack.peek() == board[i][it-1]){
                        answer += 2
                        stack.pop()
                    }else{
                        stack.push(board[i][it-1])
                    }
                    board[i][it-1] = 0 
                    println("stack = $stack")
                    break
                }
                println("it = $it 이고,i =  $i 이다.")
            }
         }
        return answer
    }
}

class StackSolution2{
    fun stacksolution2(board: Array<IntArray>, moves: IntArray): Int{
        var answer = 0 
        val stack = Stack<Int>()

        moves.forEach { move ->
            val index = move -1
            run loop@ {
                board.forEachIndexed { i, _ ->
                    val k = board[i][index]
                    if(k == 0 ) return @forEachIndexed
                    if(!stack.empty() && stack.peek() == k){
                        stack.pop()
                        answer ++
                    } else{
                        stack.push(k)
                    }
                    board[i][index] = 0
                    return @loop
                }
            }
        }
        return answer *2
    }
}