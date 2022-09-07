fun main() {
    val name = "AbdullAh"

    println(name)


    println(name.length)
    // NOTE: plus does not effect the value it returns a new string!
    println(name.plus(" Alharbi"))
    println(name.get(4))

    // this variable still hold "Abdullah"
    println(name)

    println(name.equals("ABDULLAH"))
    println(name.hashCode())
    println(name.replaceFirst("A", "a"))
    println(name.reversed())
    println(name.uppercase())
    println(name.lowercase())
    println(name.removeRange(0, 5))
}