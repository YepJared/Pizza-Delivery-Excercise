import UniqueHouses

f = open('PizzaDeliveryInput.txt', 'r')

commands = f.read()

U = UniqueHouses.Uniques(commands, 1)

print("%s houses receive at least 1 pizza with 1 delivery person." % (U))

U = UniqueHouses.Uniques(commands, 2)

print("%s houses receive at least 1 pizza with 2 delivery people." % (U))

f.close()
