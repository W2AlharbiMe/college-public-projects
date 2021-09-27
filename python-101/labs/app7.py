total = 0

while True:
    number = int(input("Enter a number (enter -1 to exit): "))

    if number < 0:
        break

    total += number

print("Total: {}".format(total))
