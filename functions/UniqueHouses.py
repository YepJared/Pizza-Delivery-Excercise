import classes.DeliveryPeople as DelP


# function to determine the number of houses that receive at least one pizza
# function is generalized for however many delivery people are available
def Uniques(commandString, people):

    # the starting house (coord 0,0) always receives at least one pizza
    houses = [[0, 0]]

    # create an array of employees to hold each of their current coordinates
    # assume starting coordinate is (0, 0) for all employees
    employees = [DelP.Deliverer(0, 0) for _ in range(people)]

    # for each command in the input string, update the current position of the
    # employee and then determine if the house they are at has been visited
    # before. If it hasn't, add that houses coordinate to house array
    for i in range(len(commandString)):

        # used to determine which employee needs to move for which command
        temp = i % people

        # update the postion of the employee who needs to move
        employees[temp].update_pos(commandString[i])

        # record new position of the employee
        coords = [employees[temp].x, employees[temp].y]

        # if a house receieves its first pizza, add the house's coordinates
        # to the array
        if coords not in houses:
            houses.append(coords)

    # the number of items in the house array is the number of houses that
    # received at least one pizza
    return len(houses)
