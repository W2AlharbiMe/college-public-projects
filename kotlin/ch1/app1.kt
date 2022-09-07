fun main() {
    print("Enter a number between 1 to 7 to view the day: ")
    var dayOfWeek = readLine()!!.toInt()

    when(dayOfWeek) {
        1 -> println("Monday")
        2 -> println("Tuesday")
        3 -> println("Wednesday")
        4 -> println("Thursday")
        5 -> println("Friday")
        6 -> println("Saturday")
        7 -> println("Sunday")
        else -> println("Invalid Day")
    }


    println("---------------------------------")

    when (dayOfWeek) {
        1, 2, 3, 4, 5 -> println("(Weekday)")
        6, 7 -> println("(Weekend)")
        else -> println("Invalid Day")
    }

    print("Enter the day of the month: ")
    var dayOfMonth = readLine()!!.toInt()
    when(dayOfMonth) {
        in 1..7 -> println("We're in the first Week of the Month")
        in 15..21 -> println("We're not in the third week of the Month")
        else -> println("none of the above")
    }


    println("-----------------------------------------------------")
    var x : Any = readLine()!!
    when(x) {
        is Int -> println("$x is an Int")
        is String -> println("$x is a String")
        !is Double -> println("$x is not Double")
        else -> println("none of the above")
    }

    println("-----------------------------------------------------")


    var number = 200
    when {
        number < 0 -> println("$number is less than zero")
        number % 2 == 0 -> println("$number is even")
        number > 100 -> println("$number is greater than 100")
        else -> println("None of the above")
    }

}
