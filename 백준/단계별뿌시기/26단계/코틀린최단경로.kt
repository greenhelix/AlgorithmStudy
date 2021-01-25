import java.io.*
import java.util.*
import kotlin.collections.ArrayList

private lateinit var arr: ArrayList<ArrayList<Node>>
private lateinit var dist: IntArray
private lateinit var vis: BooleanArray
private val queue = PriorityQueue<Node>()
private const val INF = 1000000000
private lateinit var st: StringTokenizer

data class Node(val index: Int, val dist: Int): Comparable<Node>{
    override fun compareTo(other:Node): Int = dist-other.dist
}
private fun dijkstra(start: Int){
    dist[start] = 0 
    queue.add(Node(start, 0))
    while(queue.isNotEmpty()){
        val curIndex = queue.peek().index
        val curDist = queue.peek().dist
        queue.poll()
        if(dist[curIndex]<curDist) continue
        for(i in 0 until arr[curIndex].size){
            val nextIndex = arr[curIndex][i].index
            val nextDist =curDist+ arr[curIndex][i].dist
            if(nextDist<dist[nextIndex]){
                dist[nextIndex] = nextDist
                queue.add(Node(nextIndex, nextDist))
            }
        }
    }
}
private fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    st = StringTokenizer(br.readLine())
    val n = st.nextToken().toInt()
    val e = st.nextToken().toInt()
    arr= ArrayList()
    for(i in 0 until n) arr.add(ArrayList())
    dist = IntArray(n){INF}
    vis = BooleanArray(n)
    st = StringTokenizer(br.readLine())
    val k = st.nextToken().toInt() -1
    for(i in 0 until e){
        st = StringTokenizer(br.readLine())
        val u = st.nextToken().toInt()-1
        val v = st.nextToken().toInt()-1
        val w = st.nextToken().toInt()
        arr[u].add(Node(v,w))
    }

    dijkstra(k)
    dist.forEach { if(it == INF) {
        bw.write("INF") 
        bw.write("\n")
    }else{
        bw.write(it.toString())
        bw.write("\n")
    }
bw.flush()
bw.close()}
}