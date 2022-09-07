fun main() {
    print("Enter First Number: ")
    val num1:Int = readLine()!!.toInt()
    if(num1 % 2 === 0) {
        println("Even")
    } else {
        println("Odd")
    }
}
