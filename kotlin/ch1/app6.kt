fun main() {
    var x = 1
    var y = 1

    while(x<=5) {
        y = 1
        while(y<=3) {
            println("$x * $y = "+x*y)
            y++
        }
        x++
        println("----------------")
    }
}
