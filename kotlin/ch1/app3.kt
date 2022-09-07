fun main() {


    println("1..25 -------------------------------")
    for(i in 1..25) {
        println(i)
    }

    println("until -------------------------------")

    // until
    for(i in 1 until 5) {
        println(i)
    }

    println("downTo -------------------------------")

    // downTo
    for(i in 25 downTo  0) {
        println(i)
    }

    println("step -------------------------------")

    // downTo
    for(i in 2..20 step 2) {
        println(i)
    }

    println("others 1 -------------------------------")

    var letters="A".."W"

    print("Enter Any Letter: ")
    val l = readLine()!!.uppercase()

    println(letters.contains(l))
    println(letters.hashCode())



    println("others 2 -------------------------------")
    print("Enter a number between 1..50: ")
    val num:Int = readLine()!!.toInt()

    if(num in 1..50) {
        println("The number $num is between 1..50")
    } else {
        println("The number $num is not between 1..50")
    }
}
