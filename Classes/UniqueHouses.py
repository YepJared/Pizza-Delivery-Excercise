import DeliveryPeople


def Uniques(commandString, people):
    houses = [[0, 0]]

    employees = [_ for _ in range(people)]

    for j in range(len(employees)):
        employees[j] = DeliveryPeople.Deliverer(str(j), 0, 0)

    for i in range(len(commandString)):
        employees[i % people].update_pos(commandString[i])

    return len(houses)
