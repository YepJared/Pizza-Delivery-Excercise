# Define a class that contains the coordinates of each delivery driver
class Deliverer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # function to update the coordinates of a delivery person
    def update_pos(self, direction):
        match direction:
            # South
            case "v":
                self.y -= 1

            # East
            case ">":
                self.x += 1

            # North
            case "^":
                self.y += 1

            # West
            case "<":
                self.x -= 1

            # Indicate if there is an incorrect input value and what it is
            case _:
                print("Incorrect command in Input of value %s" % (direction))
                quit()
