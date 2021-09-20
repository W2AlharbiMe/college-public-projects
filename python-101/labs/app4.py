number = int(input("Enter integer number: "))

if number > 0:

    if number % 2 == 0:
        print("Positive(Even): {0}".format(number))
    else:
        print("Positive(Odd): {0}".format(number))

elif number < 0:
    if number % 2 == 0:
        print("Negative(Even): {0}".format(number))
    else:
        print("Negative(Odd): {0}".format(number))

elif number == 0:

    if number % 2 == 0:
        print("Positive(Even): {0}".format(number))
    else:
        print("Positive(Odd): {0}".format(number))

else:
    print("invalid number")

