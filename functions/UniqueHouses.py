import classes.DeliveryPeople as DelP


def Uniques(commandString, people):
    houses = [[0, 0]]

    employees = [_ for _ in range(people)]

    for j in range(len(employees)):
        employees[j] = DelP.Deliverer(str(j), 0, 0)

    for i in range(len(commandString)):
        temp = i % people

        employees[temp].update_pos(commandString[i])

        coords = [employees[temp].x, employees[temp].y]

        if coords not in houses:
            houses.append(coords)

    return len(houses)
