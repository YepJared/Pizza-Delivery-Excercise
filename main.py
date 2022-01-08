import functions.UniqueHouses as UniH

# Ask for address of input file
address = input("Please enter file address: ")

# Take the last 4 characters of the address string to help determine file type
type = address[len(address) - 4:]

# Only continue running code if the file type is .txt
if type != ".txt":
    print("Wrong file type. Please input a \".txt\" file")
    quit()
else:
    f = open(address, 'r')

    commands = f.read()

    U = UniH.Uniques(commands, 1)

    print("%s houses receive at least 1 pizza with 1 delivery person." % (U))

    U = UniH.Uniques(commands, 2)

    print("%s houses receive at least 1 pizza with 2 delivery people." % (U))

    f.close()
