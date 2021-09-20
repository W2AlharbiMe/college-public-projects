
mass = float(input("Enter object mass: "))


weight = mass * 9.8

if weight > 500:
    print("Weight({:.2f}) object too heavy".format(weight))
elif weight < 100:
    print("Weight({:.2f}) object too light".format(weight))
else:
    print("Weight({:.2f}) object less than 100 and 500".format(weight))

 
