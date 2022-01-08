class Deliverer:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name

    def __repr__(self):
        print("%s" % (self.name))

    def update_pos(self, direction):
        match direction:
            case "v":
                self.y -= 1
            case "/>":
                self.x += 1
            case "/^":
                self.y += 1
            case "/<":
                self.x -= 1
