NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"
MOVES = [NORTH, EAST, SOUTH, WEST]
LEFT = "L"
RIGHT = "R"
TURNS = [LEFT, RIGHT]
FORWARD = "F"


class WPShip:

    def __init__(self, north, east, wp_north, wp_east):
        self.north = north
        self.east = east
        self.wp_north = wp_north
        self.wp_east = wp_east

    def __str__(self):
        return f"Ship: {self.north} North and {self.east} East, WP:  {self.wp_north} North and {self.wp_east} East."

    def exec_command(self, *args):
        command = args[0]
        param = args[1]
        if command in MOVES:
            self.move(command, param)
        elif command in TURNS:
            self.turn(command, param)
        elif command == FORWARD:
            self.forward(param)

    def move(self, direction, distance):
        if direction == NORTH:
            self.wp_north += distance
        elif direction == EAST:
            self.wp_east += distance
        elif direction == SOUTH:
            self.wp_north -= distance
        elif direction == WEST:
            self.wp_east -= distance

    def turn(self, direction, degrees):
        if degrees == 180:
            self.wp_north = (-1) * self.wp_north
            self.wp_east = (-1) * self.wp_east
        elif (direction == RIGHT and degrees == 90) or (direction == LEFT and degrees == 270):
            wpe = self.wp_east
            wpn = self.wp_north
            self.wp_north = (-1) * wpe
            self.wp_east = wpn
        else:
            wpe = self.wp_east
            wpn = self.wp_north
            self.wp_north = wpe
            self.wp_east = (-1) * wpn

    def forward(self, distance):
        self.north += self.wp_north * distance
        self.east += self.wp_east * distance