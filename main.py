import functions.UniqueHouses as UniH

f = open('PizzaDeliveryInput.txt', 'r')

commands = f.read()

U = UniH.Uniques(commands, 1)

print("%s houses receive at least 1 pizza with 1 delivery person." % (U))

U = UniH.Uniques(commands, 2)

print("%s houses receive at least 1 pizza with 2 delivery people." % (U))

f.close()
