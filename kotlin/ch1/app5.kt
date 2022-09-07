fun main() {
    do {
        print("Enter your name(it must be between 3 to 10 in length):")
        var name:String = readLine()!!

        var cond = name.length < 3 || name.length > 10

        if(cond) {
            println("Please enter another name")
        }

        if(!cond) {
            println("Your name is: $name with length of "+name.length)
        }

    } while (cond)
}