# Bug hunter

terminate = False
days_count = 1
total_bugs = 0

while not terminate:
    bugs = int(input("Day ({}) Enter the number of the bugs(enter 0 to exit): ".format(days_count)))

    # terminate program if user enter 0
    if bugs == 0:
        terminate = True

    # Validation Rule

    if bugs < 0:
        print("the bugs number should be greater than 0.")
        continue

    # accumulate bugs and days
    total_bugs += bugs
    days_count += 1

print("Total Bugs is {} in {} Days".format(total_bugs, days_count))

