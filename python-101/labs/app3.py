
# sub total prices
subtotal = 0


# tax 7%
tax = 0.07

# this variable will hold the total
total = 0

# read price 5 times
for i in range(1, 6):
    price = input(f"Enter price for item #{i}: ")

    # convert price to float
    subtotal += float(price)


# calculate the total
total = subtotal + (subtotal * tax)

print("Sub totla: ", subtotal)
print(f"Tax: ", (subtotal * tax))
print(f"Total: {total}")


'''
sum = 0
tax = 0.07
total = 0


price1 = float(input("Enter price #1: "))
price2 = float(input("Enter price #2: "))
price3 = float(input("Enter price #3: "))
price4 = float(input("Enter price #4: "))
price5 = float(input("Enter price #5: "))

sum = price1 + price2 + price3 +  price4 + price5

print(f"Sub totla: {sum}")
print("Tax: ", (sum * tax))
total = sum + (sum * tax)
print(f"Total: {total}")

'''
