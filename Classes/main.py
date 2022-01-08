import UniqueHouses

f = open('Test.txt', 'r')

commands = f.read()

print(UniqueHouses.Uniques(commands, 1))
print(UniqueHouses.Uniques(commands, 2))

f.close()
